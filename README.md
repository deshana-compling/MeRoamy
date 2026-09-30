# MeRoamy — A Multimodal Travel Assistant 🌏

MeRoamy is a conversational travel assistant built with Python, Gradio, SQLite, and the Gemini API. It can search a local database of travel packages, answer follow-up questions about destinations, and generate spoken responses using text-to-speech.

## Demo

[▶️Watch the Me Roamy Demo](https://drive.google.com/file/d/158X7PgOJLRxcepSPy-XvfpwhBhS6OrcK/view?usp=sharing)

The video shows MeRoamy responding conversationally, searching the package database, and generating a spoken response.

## Features

* 💬 Conversational travel assistant powered by Gemini
* 🔎 Tool calling to search travel packages from a local SQLite database
* 🔊 Text-to-speech responses
* 🖥️ Gradio interface for interacting with the assistant

[MeRoamy Gradio UI](meroamy_gradioui.png)


## How It Works

MeRoamy combines an LLM with a local travel-package database.

![MeRoamy Pipeline](meroamy_pipeline.jpg)

When a user asks about a destination, Gemini can decide to call the `search_packages` tool. The tool searches the SQLite database and returns the relevant package information to the user in voice and textual formats.

## Tech Stack

* **Python**
* **Gradio** — user interface
* **SQLite** — local travel-package database
* **Gemini API** — conversational LLM and text-to-speech
* **OpenAI Python SDK** — used with Gemini's OpenAI-compatible API endpoint
* **uv** — Python project and dependency management
* **python-dotenv** — environment variable management

## Project Structure

```text
multimodal_travel_assistant/
├── app.py                 # Gradio interface and main chat function.
├── database.py            # SQLite database creation and search functions.
├── prompts.py             # System prompt for the travel assistant
├── tools.py               # Tool schema and tool-call handling
├── multimodal.py          # Gemini text-to-speech functionality
├── meroamy_packages.db    # SQLite database containing travel packages
├── pyproject.toml         # Project dependencies and configuration
└── uv.lock                # Locked dependency versions
```

## Running Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd MeRoamy
```

### 2. Install dependencies

This project uses `uv` for dependency management.

```bash
uv sync
```

### 3. Add your Gemini API key

Create a `.env` file in the project directory:

```text
GEMINI_KEY=your_gemini_api_key
```

### 4. Run the application

```bash
uv run app.py
```

Gradio will launch the application locally.

## Database

The SQLite database contains four example travel packages:

| Package            | Destination                | Duration | Price |
| ------------------ | -------------------------- | -------: | ----: |
| Lavish Lakshwadeep | Lakshwadeep Islands, India |   8 days |   699 |
| Paris Explorer     | Paris, France              |   5 days |   899 |
| Japan Jewels       | Japan                      |  10 days |  2199 |
| Bali Escape        | Bali, Indonesia            |   6 days |   799 |

This project uses synthetic travel-package data for demonstration purposes. Prices are illustrative and not real booking prices.

## API Key & Security

This project requires a Gemini API key to run the LLM and text-to-speech functionality.

**Do not commit your API key to GitHub.**

The application reads the key from the `GEMINI_KEY` environment variable. Anyone running the project locally should provide their own API key.

## Future Improvements

* Adding more destinations and travel packages
* Connecting the assistant to live travel information
* Adding additional tools such as weather or flight search
* Adding AI Itinerary planning
* Adding additional input/output modalities such as images/documents.
