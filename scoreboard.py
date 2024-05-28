from turtle import Turtle
SCOREBOARD_LOC = (0, 270)
ALIGNMENT = 'Center'
FONT =('Arial', 18, 'normal')
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(SCOREBOARD_LOC[0], SCOREBOARD_LOC[1])
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
