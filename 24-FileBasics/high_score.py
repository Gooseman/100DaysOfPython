
class HighScore:
    _high_score_file = "high_score.txt"

    def __init__(self):
        self.high_score = self._load_high_score()
    
    def _load_high_score(self):
        try:
            with open(self._high_score_file, "r") as file:
                return int(file.read())
        except FileNotFoundError:
            print("High score file not found. Starting with a high score of 0.")
            return 0
    
    def update_high_score(self, score):
        print(f"Current score: {score}, High score: {self.high_score}")
        if score > self.high_score:
            self.high_score = score
            self._save_high_score()
    
    def _save_high_score(self):
        with open(self._high_score_file, "w") as file:
            file.write(str(self.high_score))
    