
class Player:
    VERSION = "1.2"

    def betRequest(self, game_state):
        me = int(game_state["in_action"])
        card1 = game_state["players"][me]["hole_cards"][0]
        card2 = game_state["players"][me]["hole_cards"][1]



        if card1["rank"] == card2["rank"]:
            return 100
        else:
            return game_state["current_buy_in"]-game_state["players"][me]["bet"]

    def showdown(self, game_state):
        pass

