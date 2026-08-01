# Bard

> AI-driven, open-ended text adventures where every turn is shaped by your choices.

Bard is a turn-based text adventure game powered by large language models. Players enter a base prompt to set the scene, then take actions in natural language. The LLM interprets each action and plans the next narrative beat, producing a dynamic, ever-branching story.

Optional **image generation** can illustrate the current scene, and **text-to-speech (TTS)** can read descriptions and character dialogue aloud in distinct voices.

---

## Features

- **Open-ended adventures**: Start with any premise — fantasy quest, sci-fi exploration, mystery, or your own custom setting.
- **Turn-based play**: Enter any action in plain text; the LLM reacts and advances the story.
- **Dynamic narration**: The game state and narrative evolve based on your choices, not a fixed script.
- **Optional image generation**: Visualise the current scene on demand.
- **Optional TTS**: Have scenes and dialogue read out in character voices.
- **Modular design**: Swap LLM providers, image generators, and TTS engines with minimal changes.

---

## How it works

1. The player provides a **base prompt** that sets the genre, setting, and initial situation.
2. Bard sends the prompt to an LLM, which returns the opening scene.
3. The player enters an **action** in natural language.
4. Bard updates the conversation context and asks the LLM to plan and write the **next sequence**.
5. Optionally, the scene is illustrated or read aloud.
6. Repeat from step 3.

---

## Tech stack

- **Python 3.14+**
- **uv** for dependency and environment management
- **just** for task running
- **ruff**, **mypy**, and **pytest** for linting, type-checking, and testing

---

## Quick start

### Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [just](https://just.systems/)

### Install

```bash
just install
```

This runs `uv sync` to create the virtual environment and install all dependencies.

### Run the game

```bash
just run
```

### Run the test suite and checks

```bash
just check
```

---

## Usage

1. Launch the game with `just run`.
2. Enter a base prompt when asked, e.g.:
   > *You are a washed-up cargo pilot who just picked up a strange distress signal from a derelict station orbiting a dead moon.*
3. When the scene is described, type any action, e.g.:
   > *Power up the ship's sensors and scan the station for life signs.*
4. The LLM will respond with the outcome and the next narrative beat.

---

## Configuration

Bard uses environment variables and a configuration file to manage API keys and optional service settings.

Create a `.env` file in the project root:

```bash
LLM_API_KEY=your_key_here
LLM_MODEL=gpt-4o

# Optional
IMAGE_GENERATION_API_KEY=your_key_here
TTS_API_KEY=your_key_here
```

A sample configuration will be added as the project grows.

---

## Project status

Bard is in early development. Core infrastructure and tooling are set up; the game loop and LLM integration are the next milestones.

### Roadmap

- [ ] Core turn-based game loop
- [ ] LLM provider abstraction
- [ ] Conversation and game state management
- [ ] Optional image generation integration
- [ ] Optional TTS integration
- [ ] Save/load adventures
- [ ] Web or TUI interface

---

## Development

Common tasks are defined in the `Justfile`:

| Command | Description |
|--------|-------------|
| `just run` | Run the game |
| `just test` | Run pytest |
| `just fmt` | Format code with ruff |
| `just lint` | Lint code with ruff |
| `just typecheck` | Type-check with mypy |
| `just check` | Run all checks |

