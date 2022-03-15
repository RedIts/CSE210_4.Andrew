from ast import Try
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
        self.is_playing = True
        self.card_values = []

        for i in range(2):
            card = Hilo()
            self.card.append(card)

    def start_game(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.update_cards()
            self.get_input()
            self.do_output()
        
    def update_cards(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        self.card_values = []

        for i in range(len(self.card)):
            card = self.card[i]
            card.shuffle()
            self.card_values.append(card.value)

        self.card_values = [int(i) for i in self.card_values]
        print(f"\nThe card is {self.card_values[0]}")

    def get_input(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        try:
            answer = input("Higher or lower? [h/l] ").lower().strip()

            if answer == 'h':
                self.score += 100 if self.card_values[1] > self.card_values[0] else -75 

            elif answer == 'l':
                self.score += 100 if self.card_values[1] < self.card_values[0] else -75

            else:
                raise Exception

        except Exception:
            print("Oops! it looks like you din't select the right choise. Remember to use 'h' for HIGHER or 'l' for LOWER")


    def do_output(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        print(f"Next card was: {self.card_values[1]}")
        print(f"Score is: {self.score}")
        self.continue_game(self.score)
    
    def continue_game(self,score):
        """ Asks if the player wants to continue
        
        Args:
            self(Director): an instance of director
        """
        try:
            play_again = ""
            if score > 0: 
                play_again = input("Play again?[y/n] ").lower().strip()

                if (play_again == "no" or play_again == "n") : 
                    print("Game Over")
                    self.is_playing = False
                
                elif (play_again == "y" or play_again == "yes") :
                    self.is_playing = True  

                else:
                    raise Exception

            elif score <= 0 :
                self.is_playing = False
                print("Game Over")
    
        except Exception:
            print("Oops! Remember to mar y/n to continue playing or not")