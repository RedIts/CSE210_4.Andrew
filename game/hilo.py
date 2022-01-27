import random

class Hilo:
    """Card guessing game from 1-13.
    Responsibility of Hilo is to draw cards and calculate points based on user answer.
    Attributes:
        value (int): card number
    """

    def __init__(self):
        """Constructs new instance of Hilo
        Args:
            self(Hilo): An instance of Hilo
        """
        self.value = 0

    def shuffle(self):
        """Generates a new random value and calculates the points for the card.
        
        Args:
            self (Hilo): An instance of Hilo.
        """
        self.value = random.randint(1, 13)

    