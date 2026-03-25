<!-- BlackRoad SEO Enhanced -->

# RoadCode

> Part of **[BlackRoad OS](https://blackroad.io)** — Sovereign Computing for Everyone

[![BlackRoad OS](https://img.shields.io/badge/BlackRoad-OS-ff1d6c?style=for-the-badge)](https://blackroad.io)
[![BlackRoad-AI](https://img.shields.io/badge/Org-BlackRoad-AI-2979ff?style=for-the-badge)](https://github.com/BlackRoad-AI)

**RoadCode** is part of the **BlackRoad OS** ecosystem — a sovereign, distributed operating system built on edge computing, local AI, and mesh networking by **BlackRoad OS, Inc.**

### BlackRoad Ecosystem
| Org | Focus |
|---|---|
| [BlackRoad OS](https://github.com/BlackRoad-OS) | Core platform |
| [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc) | Corporate |
| [BlackRoad AI](https://github.com/BlackRoad-AI) | AI/ML |
| [BlackRoad Hardware](https://github.com/BlackRoad-Hardware) | Edge hardware |
| [BlackRoad Security](https://github.com/BlackRoad-Security) | Cybersecurity |
| [BlackRoad Quantum](https://github.com/BlackRoad-Quantum) | Quantum computing |
| [BlackRoad Agents](https://github.com/BlackRoad-Agents) | AI agents |
| [BlackRoad Network](https://github.com/BlackRoad-Network) | Mesh networking |

**Website**: [blackroad.io](https://blackroad.io) | **Chat**: [chat.blackroad.io](https://chat.blackroad.io) | **Search**: [search.blackroad.io](https://search.blackroad.io)

---


> Canonical RoadCode workspace and automation hub for BlackRoad-AI.

Part of the [BlackRoad OS](https://blackroad.io) ecosystem — [BlackRoad-AI](https://github.com/BlackRoad-AI)

---

# BlackRoad-AI — RoadCode

> AI Models & Inference division of [BlackRoad OS, Inc.](https://github.com/BlackRoad-OS-Inc)

Local-first AI inference, model training, and agent orchestration. 67 agents across 7 nodes. Every model runs on your device, your data, your agents. No external AI dependencies.

**Domain**: [blackroadai.com](https://blackroadai.com)

## Products

| Product | What It Does |
|---------|-------------|
| **Lucidia** | Core AI personality — powers tutoring, chat, code assist |
| **Meridian** | Multi-agent orchestrator — routes tasks to the right model on the right node |
| **Black Mode** | Dark-themed inference UI for local model interaction |
| **AI Router** | FastAPI gateway on :7000 — load balances across fleet Ollama instances |

## Model Fleet

| Node | Models | Accelerator |
|------|--------|------------|
| **Cecilia** (.96) | 16 Ollama models | Hailo-8 (26 TOPS) |
| **Octavia** (.101) | 227 available models | Hailo-8 (26 TOPS) |
| **Lucidia** (.38) | Ollama instance | CPU |
| **Gematria** | 6 Ollama models | CPU |

**Total**: 52 TOPS of local inference, 50 AI skills across 6 modules.

## Org Hierarchy

```
BlackRoad-OS-Inc (Parent — 254 repos, 67 agents, 7 nodes)
  └── BlackRoad-AI (AI Models & Inference)
      ├── RoadCode          ← this repo (workspace + automation)
      ├── meridian           ← multi-agent orchestrator
      ├── black-mode         ← inference UI
      ├── operator           ← CLI tools + model management
      └── source             ← training data + fine-tune configs
```

## Repos in This Org

- [`RoadCode`](https://github.com/BlackRoad-AI/RoadCode) — Workspace hub (this repo)
- [`meridian`](https://github.com/BlackRoad-AI/meridian) — Agent orchestration engine
- [`black-mode`](https://github.com/BlackRoad-AI/black-mode) — Local inference UI
- [`operator`](https://github.com/BlackRoad-AI/operator) — CLI + model management
- [`source`](https://github.com/BlackRoad-AI/source) — Source tree

## RAG Pipeline

- **Qdrant** on Alice — vector search for academic citations + moral context
- **nomic-embed-text** — embedding model for document indexing
- **1,383 indexed entries** from 23 indexers, 28 entity types via unified search

## How It Connects

- **Parent**: [BlackRoad-OS-Inc](https://github.com/BlackRoad-OS-Inc) — central coordination
- **Hardware**: [BlackRoad-Hardware](https://github.com/BlackRoad-Hardware) — Hailo-8 accelerators + Pi fleet
- **Education**: [BlackRoad-Education](https://github.com/BlackRoad-Education) — Lucidia powers RoadWork tutoring
- **Foundation**: [BlackRoad-Foundation](https://github.com/BlackRoad-Foundation) — Amundson constants in training
- **Labs**: [BlackRoad-Labs](https://github.com/BlackRoad-Labs) — experimental models graduate here

## License

Proprietary — BlackRoad OS, Inc. See [LICENSE](./LICENSE).

---

*Remember the Road. Pave Tomorrow.*
