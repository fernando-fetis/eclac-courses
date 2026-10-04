'''Write corpus.txt from the English flagship reports of the ECLAC repository.

repositorio.cepal.org runs DSpace, which keeps a plain text rendering of every PDF so that its search index can read it. That rendering is what this script downloads: one request per report, and no PDF parsing anywhere.

Downloading is the easy half. The text arrives out of a two column layout, with running headers, statistical tables, credit pages and a publications catalog folded into the prose, so most of what follows decides, first line by line and then sentence by sentence, what somebody actually wrote and what is furniture. What survives is one sentence per line, which is what the notebook reads.

The PDF each report came from is kept in .temp/, which git ignores.

    python3 build-corpus.py           write corpus.txt
    python3 build-corpus.py --list    show what would be downloaded
'''

import collections
import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request
from collections.abc import Iterator

API = 'https://repositorio.cepal.org/server/api'
CORPUS = pathlib.Path(__file__).resolve().parent / 'corpus.txt'
PDFS = pathlib.Path(__file__).resolve().parent / '.temp'
AGENT = 'eclac-courses/1.0 (teaching material; fernando.fetis@uchile.cl)'

# The annual flagship reports: the same register, written by the same divisions over three decades, which is what makes a small model sound like any of them.
SERIES = [
    'Economic Survey of Latin America and the Caribbean',
    'Preliminary Overview of the Economies of Latin America and the Caribbean',
    'Social Panorama of Latin America',
    'Foreign Direct Investment in Latin America and the Caribbean',
    'Latin America and the Caribbean in the World Economy',
]
PER_SERIES = 6
CANDIDATES = 40

# Below this the item is a summary, a briefing or a single chapter.
SMALLEST = 300_000

# The first pages are the cover, the credits and the table of contents; the last ones are the publications catalog. Neither is prose anybody wrote in a paragraph.
MARGIN = 0.05

# A line that repeats this often is a running header or footer.
REPEATS = 8

SENTENCE = re.compile(r'(?<=[.!?])\s+(?=[A-Z"“])')
HYPHEN = re.compile(r'(\w)-\n(\w)')
SPACES = re.compile(r'\s+')
# Captions, notes and source lines sit in the same text stream as the prose, and a sentence that touches one of them is a splice rather than a sentence.
NOISE = re.compile(r'https?://|www\.|@|\|{2,}|\.{4,}|©|ISBN|LC/[A-Z]|\b(?:Source|Note|Figure|Table|Box|Chart|Annex)\b|\son the basis of\s| [a-h]/')


def get(url: str, **parameters: str | int) -> bytes | dict:
    if parameters:
        url = f'{url}?{urllib.parse.urlencode(parameters)}'
    request = urllib.request.Request(url, headers={'User-Agent': AGENT})
    with urllib.request.urlopen(request, timeout=90) as response:
        payload = response.read()
    return payload if url.endswith('content') else json.loads(payload)


def value(item: dict, field: str) -> str:
    entries = item['metadata'].get(field, [{}])
    return entries[0].get('value', '')


def reports(series: str) -> Iterator[dict]:
    '''The English items of one series whose title really is that series.'''
    found = get(f'{API}/discover/search/objects', query=series, dsoType='item', size=CANDIDATES, **{'f.language': 'eng,equals'})
    for entry in found['_embedded']['searchResult']['_embedded']['objects']:
        item = entry['_embedded']['indexableObject']
        if value(item, 'dc.title').lower().startswith(series.lower()):
            yield item


def bitstream(item: dict, bundle_name: str) -> tuple[str | None, str | None, int]:
    '''The href, name and size of the first file in one bundle of an item.'''
    bundles = get(item['_links']['bundles']['href'])['_embedded']['bundles']
    for bundle in bundles:
        if bundle['name'] != bundle_name:
            continue
        listed = get(bundle['_links']['bitstreams']['href'])
        for entry in listed['_embedded']['bitstreams']:
            return entry['_links']['content']['href'], entry['name'], entry['sizeBytes']
    return None, None, 0


def catalog() -> Iterator[tuple[str, str, str, dict]]:
    '''One entry per report worth downloading, newest first within a series.'''
    for series in SERIES:
        chosen = []
        for item in reports(series):
            href, _, size = bitstream(item, 'TEXT')
            if href and size >= SMALLEST:
                title = value(item, 'dc.title')
                print(f'found  {size / 1e6:5.1f} MB  {title[:70]}')
                chosen.append((title, value(item, 'dc.date.issued')[:4], href, item))
            time.sleep(0.2)
            if len(chosen) == PER_SERIES:
                break
        yield from chosen


def useful_lines(text: str) -> Iterator[str]:
    '''Drop running headers, page numbers and the rows of statistical tables.'''
    lines = text.split('\n')
    seen = collections.Counter(line.strip() for line in lines)
    for line in lines:
        stripped = line.strip()
        if not stripped or seen[stripped] >= REPEATS:
            continue
        letters = sum(character.isalpha() for character in stripped)
        if letters < 0.55 * len(stripped.replace(' ', '')):
            continue
        if not any(character.islower() for character in stripped):
            continue
        yield stripped


def is_prose(sentence: str) -> bool:
    '''A sentence somebody wrote, rather than a caption, a list or a heading.'''
    words = sentence.split()
    if not 12 <= len(words) <= 60 or not sentence.endswith('.'):
        return False
    if not sentence[:1].isupper():
        return False
    if NOISE.search(sentence):
        return False
    packed = sentence.replace(' ', '')
    letters = sum(character.isalpha() for character in sentence)
    digits = sum(character.isdigit() for character in sentence)
    if letters < 0.75 * len(packed) or digits > 0.10 * len(sentence):
        return False
    capitalized = sum(word[:1].isupper() for word in words)
    return capitalized <= 0.35 * len(words)


def sentences(text: str) -> Iterator[str]:
    body = text[int(MARGIN * len(text)):int((1 - MARGIN) * len(text))]
    joined = SPACES.sub(' ', ' '.join(useful_lines(HYPHEN.sub(r'\1\2', body))))
    for sentence in SENTENCE.split(joined):
        sentence = sentence.strip()
        if is_prose(sentence):
            yield sentence


def main() -> None:
    listing = '--list' in sys.argv
    kept = {}

    PDFS.mkdir(exist_ok=True)

    for title, year, href, item in catalog():
        if listing:
            print(f'{year}  {title[:78]}')
            continue

        raw = get(href).decode('utf-8', errors='replace')
        before = len(kept)
        kept.update(dict.fromkeys(sentences(raw)))
        print(f'{year}  {len(kept) - before:>5} sentences  {title[:60]}')

        source, name, _ = bitstream(item, 'ORIGINAL')
        if source:
            (PDFS / name).write_bytes(get(source))
        time.sleep(0.5)

    if listing:
        return

    CORPUS.write_text('\n'.join(kept) + '\n', encoding='utf-8')
    characters = sum(len(sentence) for sentence in kept)
    print(f'\ncorpus.txt: {len(kept):,} sentences, {characters / 1e6:.2f} MB, {characters / len(kept):.0f} characters each')


if __name__ == '__main__':
    main()
