# promptpipe

Pipe anything into an LLM from your shell

## Installation

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
```

## Features

- Streams tokens as they arrive
- Works with any OpenAI-compatible endpoint
- Reads the prompt from args or stdin
- Model and system prompt via flags or env

## Usage

```bash
chatsh explain this error < error.log
cat diff.patch | chatsh review this diff
```

## Project structure

```text
├── .github/
│   └── ISSUE_TEMPLATE/
│       └── bug_report.md
├── docs/
│   ├── development.md
│   ├── faq.md
│   ├── roadmap.md
│   └── usage.md
├── examples/
│   └── quickstart.md
├── tests/
│   └── test_smoke.py
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── SECURITY.md
├── chatsh.py
└── requirements.txt
```

## FAQ

**Is this production ready?**  
It works for my use case; review the code before relying on it.

**Why no framework?**  
The stdlib covers what this project needs.

## License

MIT licensed, see LICENSE.
