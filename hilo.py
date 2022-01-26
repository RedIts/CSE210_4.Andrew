import random


class Hilo:
    """Two cards with random numbers from 1 to 13
    The responsibility of Hilo is to keep track that the second card drawn by the dealer will be higher 
    or lower than the previous one. And calculate the points for it.
    """

    def __init__(self):
        """Constructs a new instance of Hilo.

        Args:
            self (Hilo): An instance of Hilo.
        """
        self.card1 = 0
        self.card2 = 0
        self.score = 300

    def random(self): 
        """Generates two random numbers        
        Args:
            self (Hilo): An instance of Hilo.
        """
        self.card1 = random.randint(1, 13)
        self.card2 = random.randint(1, 13)
       

      