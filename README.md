# Bhasha Mitra (भाषा मित्र)

## Problem

Most open-source LLMs are trained on formal, Devanagari-script Nepali or on English — but the way Nepalis actually communicate day-to-day online (texting, social media, casual chat) is **Romanized Nepali**: Nepali written in Latin script, frequently code-mixed with English words (e.g. *"aja ko meeting dherai boring thiyo"*). This informal register is the dominant mode of real digital communication in Nepal, yet it remains poorly supported — models trained only on formal Devanagari text struggle to understand or generate it naturally.

## Approach

This project fine-tunes **Gemma 4 E2B** (2B parameters) using **QLoRA** to build a Nepali-English code-mixed assistant that understands and responds naturally in Romanized Nepali — entirely on consumer hardware (RTX 4050, 6GB VRAM), rather than cloud infrastructure.

Since no ready-made Romanized Nepali instruction dataset exists, training data is constructed by transliterating an existing Devanagari Nepali instruction dataset ([`saillab/alpaca-nepali-cleaned`](https://huggingface.co/datasets/saillab/alpaca-nepali-cleaned)) into Roman script, with intentional informal spelling variation to reflect how Nepali is actually typed (e.g. both "cha" and "chha" for छ), rather than a single rigid phonetic mapping.

This approach follows methodology established in recent research on Romanized Nepali adaptation ([Benchmarking Linguistic Adaptation in Comparable-Sized LLMs on Romanized Nepali, 2026](https://arxiv.org/abs/2604.14171)), which fine-tuned larger models (7-8B) on cloud GPUs. This project applies the same core idea at a smaller scale (2B, single consumer GPU), with an emphasis on a practical, narrow-use-case assistant and a hand-evaluated comparison of base vs. fine-tuned model outputs, rather than benchmark-only evaluation.

---

## Setup

Create a virtual environment before installing project dependencies. The environment is stored in `.venv/`, which is excluded from Git.

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install indic-transliteration
```

### Windows

Open PowerShell in the project directory:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install indic-transliteration
```

If PowerShell blocks activation scripts, allow them for the current user and run the activation command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

To leave the virtual environment on either operating system:

```text
deactivate
```

## Test Transliteration

With the virtual environment activated, run the example script from the project directory:

```bash
python explore_transliteration.py
```

On Windows Command Prompt, activate the environment with `.venv\Scripts\activate.bat` first, then run the same Python command. The script prints the ITRANS transliteration of a sample Devanagari Nepali sentence.
