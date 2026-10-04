# Demonstration prompts

## 1. A chat assistant

Drag the 12 files in `data/` into the chat and paste this.

```text
Here are 12 files with social, economic and environmental indicators for 21 countries in Latin America and the Caribbean, from 2000 to 2025. Different teams put them together in different years, so they are messy: Excel and CSV are mixed, each one is organized its own way, and the same country is spelled differently depending on the file.

First, review them and tell me what problems there are for combining them. I want concrete cases, with the file and the row: country names that don't match, missing data (you'll see it isn't always marked the same way), figures that seem to measure the same thing but are on different scales, values that are out of the order of magnitude of their series, and duplicated rows. Two of the files are not data but reference material, country_codes.csv and indicator_dictionary.xlsx: use them.

Then put what you need into a tidy table and answer one question, actually computing it rather than eyeballing it: how did poverty and inequality change between 2000 and 2025, and are the countries that reduced one the most the same ones that reduced the other the most?

With that, build me a dashboard to explore the data, where I can choose the indicator and compare countries.

Every time you state something, tell me which file it came from. And if the data is not enough to support what you were about to say, I'd rather you tell me than fill the gap.
```

## 2. An agent

Open `claude` inside `demo/` and paste this.

```text
Hi. The data folder has social, economic and environmental indicators for 21 countries in Latin America and the Caribbean, from 2000 to 2025, in 12 files that different teams put together in different years: Excel and CSV are mixed, the same country is spelled several ways, and some figures seem to measure the same thing but are on different scales.

Turn it into something that can actually be used. Work in stages and let me know when you finish each one, but don't ask me whether to continue, just keep going. Save everything you make in a new folder called results. And don't work in single file: as soon as the data is in order, what comes next is independent, so split the work and use subagents in parallel.

First, review the files and tell me what is wrong, with the file and the row of each case. Don't guess how countries match from one file to another, because one of the files resolves it.

Second, put everything into a single clean table, with each country identified in a single way and each figure in its correct unit, built so that it can be regenerated if new data arrives tomorrow.

Third, build me a website that opens with a double click and without installing anything: a home page with the most striking findings, a page per country, a country comparison, a map of the region colored by the indicator I choose, search and dark mode. In ECLAC blue, which is 036BAA, with interactive charts, and made to fit this data, not a template.

Fourth, add a chat to the site to ask the data questions the way one talks, answered by a real language model. My OpenAI key is in the OPENAI_API_KEY environment variable, use it. Three conditions: the key must never reach the browser, the model must not make up a single figure because the numbers always come from my table, and without a key the chat must keep working in a simpler way instead of looking broken.

Fifth, write the conclusions with the figures that support them, and a separate section on what CANNOT be concluded from this data.

And to finish, a short Typst presentation of about six slides, reusing the charts you already made. Compile it and leave me the PDF.

Five more things that apply to everything:

- If something cannot be resolved by looking at the files, decide yourself, but write it down and tell me at the end.
- If a calculation means nothing, don't show it even if it can be done.
- Don't leave any file unused.
- Don't call anything done without testing it: open the site, check that the charts appear and that the chat answers, and fix whatever fails. Tell me what you tested.
- Add something I didn't ask for that you think of, and tell me why.

When you finish, tell me how to open each thing.
```
