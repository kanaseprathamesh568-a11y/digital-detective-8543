#!/usr/bin/env python3
"""
The Digital Detective - Mission 5: Numbers and Data
Number Converter: Converts a user-provided positive decimal integer into
its binary and hexadecimal representations.
"""

def main():
    print("==========================================")
    print(" Digital Detective — Number Converter")
    print("==========================================")
    
    user_input = input("Enter a positive decimal number: ").strip()
    
    try:
        decimal_val = int(user_input)
        if decimal_val < 0:
            print("Please enter a positive integer.")
            return
            
        binary_val = bin(decimal_val)
        hex_val = hex(decimal_val)
        
        print("\n--- Conversion Results ---")
        print(f"Decimal (Base 10)     : {decimal_val}")
        print(f"Binary (Base 2)       : {binary_val}")
        print(f"Hexadecimal (Base 16) : {hex_val}")
        print("--------------------------")
        
    except ValueError:
        print(f"Error: '{user_input}' is not a valid decimal integer.")

if __name__ == "__main__":
    main()
