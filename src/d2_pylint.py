"""
Demo pylint

First install pylint: pip install pylint

Run from the terminal: ...
"""

def convert_eur_to_usd(amount):
    """
    Convert money
    """
    result = amount * 1.20
    return result


if __name__ == "__main__":
    print(convert_eur_to_usd(500))
