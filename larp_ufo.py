import time
import random

def main():
    print("=" * 40)
    print("        larp.UFO - Crypto Dashboard")
    print("=" * 40)
    
    portfolio_value = 14250.75
    assets = ["BTC", "ETH", "SOL", "UFO"]
    
    print("\n[INFO] Initializing secure connection to node...")
    time.sleep(1)
    print("[INFO] Loading portfolio assets...\n")
    
    for asset in assets:
        price = round(random.uniform(50, 3000), 2)
        change = round(random.uniform(-5.0, 8.5), 2)
        print(f"Asset: {asset:<5} | Price: ${price:<8} | 24h: {change:+.2f}%")
    
    print("-" * 40)
    print(f"Total Portfolio Value: ${portfolio_value:,.2f}")
    print("=" * 40)
    print("Dashboard active. Press back or close to exit.")

if __name__ == "__main__":
    main()
  
