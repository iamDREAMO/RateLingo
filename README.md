<div align="center">

# RateLingo

**Professional Pricing Calculator for Language Services**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com)

![RateLingo Demo](assets/screenshots/demo.gif)

</div>

---

## The Story Behind RateLingo

With over 5 years of experience as a freelance Twi-English language specialist 
covering translation, transcription, subtitling, voice-over, interpretation, 
data annotation, and data collection, one recurring challenge was pricing 
text-based projects quickly and accurately.

Every quote request meant opening a text editor or visiting an online word 
counter, cross-referencing customised rates, and manually calculating costs — 
a workflow that introduced delays. In cases where internet access was 
unavailable, responding to urgent client quote requests before work could begin 
became a bottleneck entirely.

Toward the end of my fourth year in the role, the idea for a dedicated tool 
began to take shape. Starting with a manual sketch of the desired interface and 
drawing on a background in Python development, research pointed to Tkinter and 
PyQt as viable options for building desktop applications. This became the 
motivation to learn Tkinter — and RateLingo is the result: a practical tool 
born out of a real professional need, and proudly my second desktop application 
built with Tkinter.

---

## Overview

RateLingo is a desktop pricing calculator built for freelance language service providers. It calculates accurate project quotes based on word (texts) count across translation, transcription, voice-over, and subtitling services. Available as both a GUI desktop app and a CLI tool.

---

## Features

- Four core language services with predefined per-word rates
- Real-time word and character count as you type
- Instant cost calculation with a single click
- Save and manage quote history (SQLite3)
- Dual interface - GUI (desktop) and CLI (terminal)

---

## Installation

### Prerequisites
- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/iamDREAMO/RateLingo.git
cd RateLingo

# 2. Create virtual environment
uv venv

# 3. Run the app
uv run python main.py
```

---

## Usage

### GUI (Default)
```bash
uv run python main.py
```

1. Paste or type your text in the left panel
2. Select a service from the dropdown
3. Click **Calculate Cost** to get your quote
4. Save the quote to history or calculate another

### CLI
```bash
uv run python main.py --cli
```

Follow the prompts to select a service, enter your text, and view your quote.

---

## Service Rates

| Service       | Rate per Word |
|---------------|---------------|
| Translation   | $0.08         |
| Transcription | $0.05         |
| Voice-over    | $0.20         |
| Subtitling    | $0.12         |

*Rates are configurable in `src/core.py`*

---

## Project Structure

```
RateLingo/
├── assets/
│   └── screenshots/         # App screenshots and demo GIF
├── src/
│   ├── __init__.py
│   ├── core.py              # Business logic (rates, calculations)
│   ├── cli.py               # CLI interface
│   ├── gui.py               # GUI interface (CustomTkinter)
│   └── database.py          # SQLite3 quote history
├
│   
├── main.py                  # Entry point
├── pyproject.toml           # Project metadata
└── 
```

---

## Roadmap

### v1.0.0 (Current)
- CLI interface
- GUI desktop app
- Word counting and cost calculation
- Quote history with SQLite3

### v2.0 (Future)
- [ ] Cross-platform packaging (Windows `.exe`, linux `ELF format`, macOS `.app`)
- [ ] Export quotes to PDF
- [ ] Web application version
- [ ] Custom rate profiles per client
- [ ] Invoice generation

---

## Contributing

Contributions are welcome! Follow PEP 8 guidelines with proper docstrings, comments, and meaningful commit messages.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push and open a Pull Request

---

## Author

**Benedict Kofi Amofah**
- GitHub: [@iamDREAMO](https://github.com/iamDREAMO)
- LinkedIn: [Benedict Kofi Amofah](https://www.linkedin.com/in/benedict-kofi-amofah)

## License

Licensed under the [MIT License](LICENSE).

---

<div align="center">

*Made with ❤️ for the Freelance language community*

[Report Bug](https://github.com/iamDREAMO/RateLingo/issues) · [Request Feature](https://github.com/iamDREAMO/RateLingo/issues)

</div>