# Brochure Creator

![Screenshot](/Screenshot.png)

## Langsmith Tracing

![Screenshot](/Screenshot_Tracing)

A small Python project that turns a web page into a brochure-style summary using a local LLM via Ollama and a Gradio interface.

## What this project does

The app pulls content from a URL, sends it to a local language model, and returns a brochure-like response generated from the page content.

This repository includes two lightweight demos:

- `src/brochure_creator/main.py` — brochure generator for a provided webpage URL
- `src/brochure_creator/ask-anything.py` — general Q&A Gradio app

## Tech stack

- Python 3.15+
- Gradio for the UI
- LangChain + LangChain Ollama integration
- BeautifulSoup for document parsing support
- Ollama for the local model runtime

## Project structure

```text
brochure-creator/
├── README.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── src/
│   └── brochure_creator/
│       ├── __init__.py
│       ├── main.py
│       ├── model.py
│       └── ask-anything.py
└── .venv/
```

## Prerequisites

Before running the app, install and start Ollama and pull a model such as `llama3.2:1b`:

```bash
ollama serve
ollama pull llama3.2:1b
```

You can override the default model with environment variables:

```bash
export LOCAL_LLM_MODEL=llama3.2:1b
export LOCAL_LLM_MODEL_PROVIDER=ollama
```

## Installation

This project uses `uv` for dependency management.

```bash
cd brochure-creator
uv sync
```

If you prefer a standard virtual environment:

```bash
cd brochure-creator
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Running the app

### Brochure generator

```bash
cd brochure-creator
uv run python src/brochure_creator/main.py
```

This launches a Gradio interface where you can paste a webpage URL and generate brochure content.

### Ask Anything demo

```bash
cd brochure-creator
uv run python "src/brochure_creator/ask-anything.py"
```

This runs a simple question-and-answer app powered by the same local model.

## Notes

- The Local LLM is configured in `src/brochure_creator/model.py`.
- The app expects a local Ollama model to be available on the machine.
- The generated brochure is based on the text extracted from the supplied web page and may vary depending on the model and source content.

## Typical workflow

1. Start Ollama
2. Pull a model
3. Install dependencies
4. Launch the Gradio app
5. Paste a URL or ask a question
6. Review the generated content
