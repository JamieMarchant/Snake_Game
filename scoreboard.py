from turtle import Turtle


# inherit turtle
# keep track of score and display


class ScoreBoard(Turtle):

    def __init__(self, current_score=0):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 270)
        self.current_score = current_score
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear previous score
        self.write(f"Scoreboard: {self.current_score}", False, "center", ('Courier', 12, 'normal'))

    def increment_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, "center", ('Courier', 12, 'normal'))