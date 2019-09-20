class PaperBot:
    def __init__(self):
        self.dynamite = None
        self.opponent_dynamite = None
        self.points = None

    def make_move(self, gamestate):
        return self.random_move(gamestate)

    def random_move(self, gamestate):
        rounds = len(gamestate["rounds"])
        self.update_dynamite(gamestate)
        self.update_water_balloon(gamestate)

        options = self.get_valid_options()

        self.update_points_on_offer(gamestate)

        if rounds > 900:
            if "D" in options:
                return "D"
            else:
                return options[abs(hash(str(gamestate))) % len(options)]
        else:
            return options[abs(hash(str(gamestate))) % len(options)]

    def update_dynamite(self, gamestate):
        self.dynamite = 0
        rounds = gamestate["rounds"]
        for game_round in rounds:
            if game_round["p1"] == "D":
                self.dynamite += 1

    def update_water_balloon(self, gamestate):
        self.opponent_dynamite = 0
        rounds = gamestate["rounds"]
        for game_round in rounds:
            if game_round["p2"] == "D":
                self.opponent_dynamite += 1

    def get_valid_options(self):
        options = ["R", "P", "S"]
        if self.dynamite < 100:
            options.append("D")
        if self.opponent_dynamite < 100:
            options.append("W")
        return options

    def update_points_on_offer(self, gamestate):
        self.points = 0
        rounds = gamestate["rounds"]
        for game_round in rounds:
            if game_round["p1"] == game_round["p2"]:
                self.points += 1
            elif game_round["p1"] != game_round["p2"]:
                self.points -= self.points
