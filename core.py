import sympy

class GrellgondConstant:
    def __init__(self):
        self.symbol = 'ℷ'
        self.name = "Grellgond Constant"
        # Pre-calculated to the first 15 gaps for immediate use
        self.approx = 0.1246814182022343644
        
    def __repr__(self):
        return f"{self.symbol} ({self.name}) ≈ {self.approx}"
        
    def __float__(self):
        return self.approx

    def calculate_digits(self, prime_limit=100000):
        """
        Dynamically calculates the exact digits of ℷ up to a given prime limit.
        """
        max_gap = 0
        last_prime = 2
        digits = "0."
        
        for p in sympy.primerange(3, prime_limit):
            gap = p - last_prime
            if gap > max_gap:
                max_gap = gap
                digits += str(gap)
            last_prime = p
            
        return digits

# Instantiate the constant for users to import
gimel = GrellgondConstant()
