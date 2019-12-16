
class Player:
    VERSION = "1.1"

    def betRequest(self, game_state):
        me = int(game_state["in_action"])
        if game_state["players"][me]["hole_cards"][0]["rank"] ==  game_state["players"][me]["hole_cards"][1]["rank"]:
            return 200
        else:
            return 0

    def showdown(self, game_state):
        pass

