# genpark-generative-seo-skill

> **GenPark AI Agent Skill** -- # Generative Engine SEO (GEO) Optimizer Skill

This repository contains the **Generative Engine SEO (GEO) Optimizer Skill** — a modular developer Python client SDK, agent skill interface configuration (`skill.json`), and executable workflow tests. It is designed to restructure e-commerce catalog information to maximize recommendation and citation probability on AI-driven search platforms (e.g., Perplexity AI, ChatGPT Search, Gemini).

---

## 🚀 Capabilities

* **AI Citability Scoring:** Evaluates product listing text against heuristics preferred by LLM crawlers (e.g. data density, specifications depth, comparative phrases).
* **Information Density Restructuring:** Rewrites typical marketing copy ("fluff") into structured, comparative descriptions with clear attribute specifications.
* **JSON-LD Schema Generation:** Instantly outputs valid Product structured schemas for indexing by search crawlers.

---

## 🛠️ Setup & Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configuration:
   Set your API environment variables if executing requests against the live production server (otherwise, client executes in mock mode):
   * **PowerShell**:
     ```powershell
     $env:GEO_API_KEY="your_api_key"
     ```
   * **bash**:
     ```bash
     export GEO_API_KEY="your_api_key"
     ```

---

## 💻 SDK Usage Reference

```python
from generative_seo import GenerativeSeoClient

# Initialize Client (mock mode by default)
client = GenerativeSeoClient()

# Audit content for AI search indexability
audit = client.analyze_citability(
    content="This is the most amazing widget ever made in the universe.",
    specs={"weight": "150g", "battery": "500mAh"}
)
print(f"Citability: {audit['citability_score']}")

# Optimize listing content
optimized = client.optimize_content(
    product_name="Zenith Earbuds",
    original_copy="Amazing earbuds.",
    specs={"battery": "32h", "bt_version": "5.3"}
)
print(optimized["optimized_text"])
print(optimized["schema_markup"])
```

---

## 📜 License
This project is licensed under the MIT License.