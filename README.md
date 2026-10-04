<div align="center">

# AI Lectures · ECLAC

[![ECLAC](https://img.shields.io/badge/ECLAC-United%20Nations-036BAA?style=for-the-badge)](https://www.cepal.org/en)

</div>

Slides, figures and bibliography for two lectures on artificial intelligence given at the [Economic Commission for Latin America and the Caribbean](https://www.cepal.org/en), the United Nations regional commission based in Santiago.

| Lecture | Slides | Audience |
| --- | --- | --- |
| **1 · Foundations of Generative AI**: what generative AI is, where it helps, where it fails and how to check what it produces | [`slides.pdf`](lecture-1/slides.pdf) | All staff, no prerequisites |
| **2 · Anatomy of a Language Model**: how a language model is built, trained and evaluated, with a notebook that trains one from scratch | [`slides.pdf`](lecture-2/slides.pdf) · [`notebook.ipynb`](lecture-2/demo/notebook.ipynb) | Technical; lecture 1 recommended first |

**Fernando Fetis Riquelme** · Spring 2026

## Layout

```
eclac-courses/
├── common/
│   ├── theme.typ              Palette, slide layouts and content components
│   ├── logos/                 ECLAC and United Nations marks
│   └── scripts/
│       ├── plotstyle.py       Figure palette, typeface and sizes
│       ├── diagram.py         Boxes, horizontal and vertical arrows, photos
│       └── check-overflow.py  Reports slides whose content spills onto the next page
├── lecture-1/
│   ├── slides.typ · slides.pdf
│   ├── bib.yml                Bibliography, every entry cited on some slide
│   ├── figures/               Generated figures and sourced images (provenance in its README)
│   ├── scripts/               One script per generated figure
│   └── demo/                  Live demonstration: 12 data files and prompts.md
└── lecture-2/
    ├── slides.typ · slides.pdf
    ├── bib.yml
    ├── figures/
    ├── scripts/
    └── demo/
        ├── notebook.ipynb     Trains a small GPT from scratch, then runs published models
        ├── modal-run.py       Runs the notebook on a Modal GPU
        └── assets/            Corpus, its builder (build-corpus.py) and the trained checkpoint
```

## Building

Requires [Typst](https://typst.app), Python 3.10+, and the Fira Sans, Fira Math and JetBrains Mono typefaces.

```bash
brew install typst
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make
```

| Command | What it does |
| --- | --- |
| `make` | Regenerate stale figures, then compile every deck |
| `make lecture-1` | Figures and deck for one lecture |
| `make slides` | Compile the decks, leaving the figures untouched |
| `make figures` | Regenerate every figure whose script changed |
| `make watch LECTURE=lecture-1` | Rebuild one deck on every save |
| `make check` | Report slides whose content spills onto the next page |
| `make clean` · `make clean-figures` | Remove the compiled decks or the generated figures |

Compiled decks and figures are versioned, so every PDF can be downloaded without building anything. A single figure is redrawn with `cd lecture-1/scripts && python3 timeline.py`.

## Running the notebook

Lecture 2 is shown alongside `notebook.ipynb`. Sections 1 and 2 run on a laptop (with `torch` installed); sections 3 and 4 load models of up to 8 billion parameters and need a GPU, which `modal-run.py` rents by the second from [Modal](https://modal.com) with every dependency installed in the container.

```bash
modal setup                               # once
cd lecture-2/demo
modal run modal-run.py::corpus            # rebuild assets/corpus.txt from the ECLAC repository
modal run modal-run.py::execute           # run every cell on a GPU, write the notebook back here
modal run modal-run.py::jupyter           # serve JupyterLab from the GPU, print its URL
```

**Every one of them stops with Ctrl+C in that terminal, and none of them stops on its own.** The container is billed by the second for as long as the local command is alive, whether or not a browser tab is open, up to the timeout each function declares.

`jupyter` is the one to use while teaching. Open the printed URL in a browser, or paste it into the *Jupyter: Specify Jupyter Server for Connections* command of VS Code to keep the notebook on screen locally while every cell runs on the GPU. It copies this folder up and never copies anything back, so anything run or edited there leaves the local notebook untouched. `execute` is the opposite: it overwrites the local notebook with the executed one.

The published models and the notebook live in Modal volumes, so a model is downloaded once and is already there on the next run.

### Choosing a GPU

`GPU=H100 modal run modal-run.py::jupyter` asks for a different card; the default is an L40S. The choice changes how long a cell takes and whether the models fit, never what they answer. Sections 3 and 4 hold two models of seven and eight billion parameters at the same time, about 32 GB of weights before anything else:

| GPU | Memory | Notes |
| --- | --- | --- |
| `L40S` | 48 GB | The default. Fits with room to spare, and the cheapest card that does |
| `A100-40GB` | 40 GB | Fits, with little margin |
| `A100-80GB` | 80 GB | Roomy, faster than an L40S at training |
| `H100` | 80 GB | The fastest of the common ones, and the one to take when an L40S is busy |
| `H200` | 141 GB | More memory than this notebook can use |

`T4`, `L4` and `A10G` have 16 to 24 GB and cannot hold both models. Modal publishes what each one costs per second on its [pricing page](https://modal.com/pricing).
