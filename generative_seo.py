import os
import json
import requests
from typing import List, Dict, Any, Optional

class GenerativeSeoError(Exception):
    """Base exception class for Generative SEO Client."""
    pass

class GenerativeSeoClient:
    """
    Client for auditing and rewriting product content to optimize for LLM citations.
    Supports a mock mode for local testing.
    """
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://api.generative-seo.ai/v1"):
        self.api_key = api_key or os.environ.get("GEO_API_KEY")
        self.base_url = base_url.rstrip("/")
        self.mock_mode = self.api_key is None or self.api_key == "mock"
        
        if self.mock_mode:
            print("[GenerativeSeoClient] API Key not set. Running in MOCK Mode.")

    def analyze_citability(self, content: str, specs: Dict[str, str]) -> Dict[str, Any]:
        """
        Evaluate current copy and return a score indicating citation probability by AI search engines.
        """
        if self.mock_mode:
            # Local heuristic audit simulation
            word_count = len(content.split())
            spec_count = len(specs)
            density_score = min(1.0, (spec_count * 15) / max(1, word_count))
            
            # Formulate suggestions based on heuristics
            suggestions = []
            if spec_count < 3:
                suggestions.append("Low technical specification counts. Add more structured parameters (dimensions, materials).")
            if "compare" not in content.lower():
                suggestions.append("Missing comparative reference keywords. Add contrastive benefits against industry standards.")
            if word_count > 300 and spec_count < 2:
                suggestions.append("High word count with low data density. Prune marketing jargon in favor of concrete features.")
            
            citability = round(0.4 + (density_score * 0.5), 2)
            
            return {
                "citability_score": citability,
                "metrics": {
                    "word_count": word_count,
                    "spec_density": spec_count,
                    "jargon_index": "medium"
                },
                "suggestions": suggestions if suggestions else ["Content is highly optimized for AI search engines."]
            }

        # Remote API integration call
        payload = {"content": content, "specs": specs}
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            resp = requests.post(f"{self.base_url}/audit", json=payload, headers=headers, timeout=30)
            return resp.json()
        except Exception as e:
            raise GenerativeSeoError(f"API Audit call failed: {e}")

    def optimize_content(self, product_name: str, original_copy: str, specs: Dict[str, str]) -> Dict[str, Any]:
        """
        Optimize copy to satisfy LLM crawlers and output JSON-LD structured schema markup.
        """
        if self.mock_mode:
            print(f"[Mock API] Generating GEO optimized copy for product: {product_name}")
            
            # Simulate structured output
            bullets_str = "\n".join([f"- **{k}**: {v}" for k, v in specs.items()])
            optimized_copy = (
                f"### {product_name} Factual Overview\n"
                f"The {product_name} is an advanced product designed for professional applications. "
                f"Unlike standard models, it integrates key technical specifications to ensure performance:\n\n"
                f"{bullets_str}\n\n"
                f"**Comparative Advantage**: Incorporates structural optimizations offering higher efficiency "
                f"compared to conventional designs. Optimized for seamless compatibility and high durability."
            )
            
            schema = {
                "@context": "https://schema.org/",
                "@type": "Product",
                "name": product_name,
                "description": original_copy[:150],
                "additionalProperty": [{"@type": "PropertyValue", "name": k, "value": v} for k, v in specs.items()]
            }
            
            return {
                "optimized_text": optimized_copy,
                "schema_markup": json.dumps(schema, indent=2),
                "estimated_score": 0.88,
                "changes_applied": ["Injected spec tables", "Pruned fluff adjectives", "Structured comparative cues"]
            }

        payload = {"product_name": product_name, "original_copy": original_copy, "specs": specs}
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            resp = requests.post(f"{self.base_url}/optimize", json=payload, headers=headers, timeout=30)
            return resp.json()
        except Exception as e:
            raise GenerativeSeoError(f"API Optimize call failed: {e}")
