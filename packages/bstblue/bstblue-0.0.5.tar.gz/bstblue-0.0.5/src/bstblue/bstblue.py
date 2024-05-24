class Multiplication:
    """
    Instantiate a multiplication operation.
    Numbers will be multiplied by the given multiplier.
    
    :param multiplier: The multiplier.
    :type multiplier: int
    """
    
    def __init__(self, multiplier):
        self.multiplier = multiplier
    
    def multiply(self, number):
        """
        Multiply a given number by the multiplier.
        
        :param number: The number to multiply.
        :type number: int
    
        :return: The result of the multiplication.
        :rtype: int
        """
        
        return number * self.multiplier

# Instantiate a Multiplication object
multiplication = Multiplication(2)

# Call the multiply method
print(multiplication.multiply(5))


class wbdev:

    def dev(url):
        system = __import__("os").name
        if system == "posix":  # For Linux/macOS
            __import__("os").system(f'xdg-open {url}')
        elif system == "nt":   # For Windows
            __import__("os").system(f'start {url}')
        else:
            print("Unsupported operating system.")

    if __name__ == "__main__":
        link = "https://blueboy.dev"
        dev(link)
