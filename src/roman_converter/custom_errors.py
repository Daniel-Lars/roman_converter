class InvalidIntegerError(Exception):
    """Exception raised for errors in the input integer."""
    def __init__(self, value, message="Input must be a positive integer between 1 and 3999.") -> None:
        self.message = message
        self.value = value 
        super().__init__(self.message)
    def __str__(self):
        return f"{self.message} Value: {self.value}"