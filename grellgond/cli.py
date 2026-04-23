import argparse
from .core import gimel

def main():
    parser = argparse.ArgumentParser(description="Calculate the Grellgond constant (ℷ)")
    parser.add_argument('--limit', type=int, default=100000, 
                        help='The upper prime limit for calculating maximal gaps (default: 100000)')
    
    args = parser.parse_args()
    
    print(f"Calculating ℷ (Grellgond Constant) up to prime limit {args.limit}...")
    result = gimel.calculate_digits(prime_limit=args.limit)
    print(f"\nResult: {result}")

if __name__ == '__main__':
    main()
