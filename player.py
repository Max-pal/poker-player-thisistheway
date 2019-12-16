
class Player:
    VERSION = "2.0"

    def betRequest(self, game_state):
        small_pairs = [["2", "2"], ["3", "3"], ["4", "4"], ["5", "5"], ["6", "6"], ["7", "7"]]
        medium_pairs = [["8", "8"], ["9", "9"], ["10", "10"], ["J", "J"]]
        president_pairs = [["K", "K"], ["Q", "Q"], ["A", "A"],["J","J"],["10","10"]]
        president_cards = ["K","Q","A","J","10"]

        me = int(game_state["in_action"])
        card1 = game_state["players"][me]["hole_cards"][0]
        card2 = game_state["players"][me]["hole_cards"][1]
        my_cards_rank = [card1["rank"], card2["rank"]]
        current_buy_in = int(game_state["current_buy_in"])
        players = game_state["players"]
        mybet = int(players[me]["bet"])
        minimum_raise = int(game_state["minimum_raise"])
        call = current_buy_in-mybet
        community_cards = game_state["community_cards"]
        raise_minimum = current_buy_in - mybet + minimum_raise

        if card1["rank"] in president_cards and card2["rank"] in president_cards or my_cards_rank in president_pairs or card1 in president_cards and card2 in president_cards:
            return call

        if my_cards_rank in president_pairs:
            return current_buy_in - mybet + minimum_raise + int(players[me]["stack"]*0.29)
        elif my_cards_rank in medium_pairs:
            return current_buy_in - mybet + minimum_raise + int(players[me]["stack"]*0.1)
        elif my_cards_rank in small_pairs:
            return current_buy_in - mybet + minimum_raise + int(players[me]["stack"]*0.05)
        else:
            return 0

    def showdown(self, game_state):
        pass
