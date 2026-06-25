import sys
from generative_seo import GenerativeSeoClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== Generative Engine SEO (GEO) Optimizer Example ===")
    
    # Initialize client in mock mode
    client = GenerativeSeoClient()
    
    product_name = "Zenith Wireless Earbuds"
    original_fluff_copy = (
        "Experience the magic of incredible audio with the Zenith Wireless Earbuds! "
        "It's like a symphony in your ears. Simply the most amazing and gorgeous headphones "
        "ever made in the universe. You will fall in love with them instantly."
    )
    specs = {
        "Frequency Response": "20Hz - 20kHz",
        "Battery Life": "32 Hours (with charging case)",
        "Water Resistance": "IPX7 Rating",
        "Connectivity": "Bluetooth 5.3"
    }

    # 1. Audit original copy for AI Citability
    print("\n--- Auditing Original Content ---")
    audit = client.analyze_citability(original_fluff_copy, specs)
    print(f"Initial Citability Score: {audit['citability_score']}")
    print("Audit Suggestions:")
    for suggestion in audit['suggestions']:
        print(f"  - {suggestion}")

    # 2. Optimize Copy for Generative Engines
    print("\n--- Generating GEO Optimized Product Copy ---")
    optimized = client.optimize_content(product_name, original_fluff_copy, specs)
    print("\n[Optimized Text Output]:")
    print(optimized["optimized_text"])
    
    print("\n[JSON-LD Schema Markup]:")
    print(optimized["schema_markup"])
    
    print("\nOptimization Improvements:")
    for improvement in optimized["changes_applied"]:
        print(f"  - {improvement}")
    print(f"Estimated Post-Optimization Score: {optimized['estimated_score']}")

if __name__ == "__main__":
    main()
