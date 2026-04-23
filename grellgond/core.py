import sympy

class GrellgondConstant(float):
    def __new__(cls):
        # This tells Python: "Under the hood, treat this entire class as this exact float"
        exact_string = "0.124681418202234364452728696112114118148"
        return super().__new__(cls, float(exact_string))

    def __init__(self):
        self.symbol = 'ℷ'
        self.name = "Grellgond Constant"
        self.exact_string = "0.124681418202234364452728696112114118148"
        
    def __repr__(self):
        # This is what shows up when you print the variable directly
        return f"{self.symbol} ({self.name}) ≈ {self.exact_string}..."

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