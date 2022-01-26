from game.hilo import Hilo

class Director:
    """Directs the game
    
    Attributes:
        card (List[card]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Creates new instance of Director
        
        Args:
            seelf (Director): an instance of Director.
        """
