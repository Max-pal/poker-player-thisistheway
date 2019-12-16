
class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):
        me = game_state["in_action"]
        if game_state["players"][me]["hole_cards"]["rank"] ==  game_state["players"][me]["hole_cards"]["rank"]:
            return game_state["current_buy_in"] + game_state["minimum_raise"]
        else:
            return 0

    def showdown(self, game_state):
        pass

