from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scb()

    def update_scb(self):
        self.clear()
        self.write(move=False, align='center',
                   arg=f"Score: {self.score} High Score: {self.high_score}", font=("arial", 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scb()

    def reset(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as f:
                f.write(f"{self.high_score}")
            self.high_score = self.score
        self.score = 0
        self.update_scb()
