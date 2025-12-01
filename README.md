# 🧠 My GenAI Garage

> A curated playground of hands-on GenAI notebooks, demos, and helpers for talks, workshops, and experiments.

This repo collects everything from the basics of tokenization to complete Retrieval-Augmented Generation (RAG) demos, multi-modal experiments, and evaluation utilities. Each folder is self-contained so you can cherry-pick a topic for meetups or deep dives.

---

## 📚 Table of Contents

1. [Repo Highlights](#-repo-highlights)
2. [Project Structure](#-project-structure)
3. [Getting Started](#-getting-started)
4. [Running the Demos](#-running-the-demos)
5. [Data & Environment](#-data--environment)
6. [Extending the Garage](#-extending-the-garage)
7. [Resources & References](#-resources--references)

---

## ✨ Repo Highlights

- **Story-driven layout** – From foundational concepts to advanced GenAI systems.
- **Notebook-first** – Every topic is a Jupyter notebook you can run live during a session.
- **Utility helpers** – Centralized helpers in `garage_helper/` for LLM access and shared utilities.
- **Showcase ready** – Clean Markdown blocks, emojis, and formatted outputs for stage demos.

---

## 🗂 Project Structure

```
My_GenAI_Garage/
├── 00-Foundations/          # Tokenization, embeddings, and other fundamentals
├── 01-Prompt_Engineering/   # Prompt patterns, guardrails, templates
├── 02-RAG_Systems/          # RAG foundations + simple PDF chat demos
├── 03-Agents_and_Tools/     # Tool-using agents (WIP)
├── 04-Fine_Tuning/          # Fine-tuning experiments (WIP)
├── 05-Multimodal/           # Vision, audio, and cross-modal playgrounds
├── 06-Evaluation_Ops/       # Quality checks, eval pipelines, logging
├── garage_helper/           # Shared client wrappers, utility scripts
├── data/                    # Sample PDFs / datasets (gitignored)
├── main.py                  # Quick sanity-check entry point
└── pyproject.toml           # Project metadata & dependencies
```

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/<your-handle>/My_GenAI_Garage.git
cd My_GenAI_Garage

# 2. Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies (uv preferred, fallback pip)
uv sync            # if uv is installed
# or
pip install -r requirements.txt  # if you export pip requirements later

# 4. Copy env template and add your keys
cp .env.example .env    # populate OPENAI_API_KEY, endpoints, etc.
```

> Using **uv** keeps installations fast and reproducible (see `uv.lock`).

---

## 🧪 Running the Demos

### Launch Jupyter Lab / Notebook

```bash
uv run jupyter lab         # or: uv run jupyter notebook
```

Open the notebook you want (e.g., `02-RAG_Systems/01-Simple_RAG/chat_with_pdf.ipynb`) and follow the instructions inside. Most notebooks expect:

- An `.env` with model keys (OpenAI, Azure OpenAI, Anthropic, Google, etc.)
- Data files placed under `data/` or a path adjusted in the notebook.

### Running Helper Scripts

```bash
uv run python main.py
# -> Hello from my-genai-garage!
```

The `garage_helper/llm_model.py` module exposes provider-agnostic wrappers if you want to script custom demos.

### Using Google Colab
### Notebook Index

| Topic              | Notebook                                                                                      | Colab |
|--------------------|-----------------------------------------------------------------------------------------------|-------|
| 00-Foundations     | [Intro to Tokenization](https://github.com/murugesan-vadivel/My_GenAI_Garage/blob/main/00-Foundations/01-Intro_Tokenization.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/murugesan-vadivel/My_GenAI_Garage/blob/main/00-Foundations/01-Intro_Tokenization.ipynb) |
| 01-Prompt_Engineering | [Prompt Patterns 101](https://github.com/murugesan-vadivel/My_GenAI_Garage/blob/main/01-Prompt_Engineering/01-Prompt_Patterns_101.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/murugesan-vadivel/My_GenAI_Garage/blob/main/01-Prompt_Engineering/01-Prompt_Patterns_101.ipynb) |
| 02-RAG_Systems     | [Simple PDF Chat RAG](https://github.com/murugesan-vadivel/My_GenAI_Garage/blob/main/02-RAG_Systems/01-Simple_RAG/chat_with_pdf.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/murugesan-vadivel/My_GenAI_Garage/blob/main/02-RAG_Systems/01-Simple_RAG/chat_with_pdf.ipynb) |


---

## 📦 Data & Environment

- **Data**: Keep sample PDFs or datasets inside `data/`. The folder is gitignored by default.
- **Secrets**: Store API keys in `.env`. Never commit credentials.
- **Models**: Update `garage_helper/llm_model.py` with new providers or deployments as needed.

---

## 🧩 Extending the Garage

1. **Add a notebook** under the appropriate numbered folder (or create a new module).
2. **Document inputs** at the top of the notebook (env vars, files, expected outputs).
3. **Contribute helper utilities** to `garage_helper/` if they may be reused.
4. **Update this README** with a short blurb so others can find your addition quickly.

> Looking for ideas? Try adding: Anthropic Claude recipes, AutoGen agents, LangGraph experiments, multimodal search, eval dashboards, etc.

---

## 🔗 Resources & References

- [OpenAI API Docs](https://platform.openai.com/docs)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [uv Package Manager](https://github.com/astral-sh/uv)

Enjoy the garage! Contributions and suggestions are welcome—open an issue or drop a PR whenever you build a new pit-stop. 🏎️

