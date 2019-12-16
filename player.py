
class Player:
    VERSION = "1.3"

    def betRequest(self, game_state):
        small_pairs = [["2", "2"], ["3", "3"], ["4", "4"], ["5", "5"], ["6", "6"], ["7", "7"]]
        medium_pairs = [["8", "8"], ["9", "9"], ["10", "10"], ["J", "J"]]
        president_pairs = [["K", "K"], ["Q", "Q"], ["A", "A"]]


        me = int(game_state["in_action"])
        card1 = game_state["players"][me]["hole_cards"][0]
        card2 = game_state["players"][me]["hole_cards"][1]
        my_cards_rank = [card1 + card2]
        current_buy_in = int(game_state["current_buy_in"])
        players = game_state["players"]
        mybet = int(players["in_action"]["bet"])
        minimum_raise = int(game_state["minimum_raise"])
        call = current_buy_in-mybet
        community_cards = game_state["community_cards"]
        raise_minimum = current_buy_in - mybet + minimum_raise

        if my_cards_rank in president_pairs:
            return 500
        elif my_cards_rank in medium_pairs:
            return 200
        elif my_cards_rank in small_pairs:
            return 100
        else:
            return 0
        # if card1["rank"] == card2["rank"] and len(game_state["community_cards"]) == 0:
        #     return call
        # elif card1["rank"] == card2["rank"] or self.check_card_rank_in_community_cards(card1,community_cards) or self.check_card_rank_in_community_cards(card2,community_cards):
        #     return raise_minimum
        # else:
        #     return 0

    def showdown(self, game_state):
        pass

    def check_card_rank_in_community_cards(self,card,community_cards):
        for com_card in community_cards:
            if com_card["rank"] == card["rank"]:
                return True
        return False
