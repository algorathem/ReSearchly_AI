# Einstyn – AI Research Assistant

![GitHub Workflow Status](https://img.shields.io/badge/build-passing-brightgreen)
![GitHub Repo Size](https://img.shields.io/github/repo-size/yourusername/lumina)
![License](https://img.shields.io/badge/license-MIT-blue)

## About

**Einstyn** is an AI-powered research assistant designed to help researchers quickly find, validate, summarize, and replicate sources. It combines intelligent querying, structured summaries, and optional implementation guidance for experiments.

---

## Features

- Finds relevant research sources for a query
- Provides digestible summaries in a chat-like interface
- Explains implementation steps for replicating experiments
- Supports quick actions on sources (drag, click, request implementation)
- Modular pipeline using Motia flows and steps

---

## Tech Stack

- **Backend:** Python + Motia
- **Frontend:** React
- **AI/ML:** OpenAI API, Motia LLM flows
- **Database:** PostgreSQL 
- **Architecture:** Modular pipeline: Query → Validation → Summarization → Action

---

## Installation

1. Clone the repo:
```bash
git clone https://github.com/yourusername/lumina.git
cd lumina
