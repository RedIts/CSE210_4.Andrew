from game.hilo import Hilo

class Director:
    """Directs the game
    
    Attributes:
        card (List[card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Creates new instance of Director
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = []
        self.score = 300
        # self.total_score = 300
        self.card_values = []

        for i in range(2):
            card = Hilo()
            self.card.append(card)

    def start_game(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        self.update_cards()
        self.get_input()
        self.do_output()
        
    def update_cards(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        for i in range(len(self.card)):
            card = self.card[i]
            card.shuffle()
            self.card_values.append(card.value)
        self.card_values = [int(i) for i in self.card_values]
        print(f"The card is {self.card_values[0]}")

    def get_input(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        answer = input("Higher or lower? [h/l] ")
        if answer == 'h':
            if self.card_values[1] > self.card_values[0]:
                self.score += 100
            else:
                self.score -= 75
        elif answer == 'l':
            if self.card_values[1] < self.card_values[0]:
                self.score += 100
            else:
                self.score -= 75
        else:
            self.score -= 75

    def do_output(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        print(f"Next card was: {self.card_values[1]}")
        print(f"Score is: {self.score}")

    