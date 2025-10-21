# Control the Score

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Score(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        
        with open("20thDay/HighScore.txt") as file1 :
            self.high_score = int(file1.read())

        self.color("white")
        self.penup()
        self.goto(0, 270) 
        self.hideturtle()
        self.update_score()

    def update_score(self) :
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def reset(self) :
        if self.score > self.high_score  :
            self.high_score = self.score
            with open("20thDay/HighScore.txt", "w") as file2 :
                file2.write(f"{self.high_score}")

        self.score = 0
        self.update_score()       

    def increase_score(self) :
        self.score += 1
        self.update_score()

    # def game_over(self) :
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)            
