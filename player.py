
class Player:
    VERSION = "1.3"

    def betRequest(self, game_state):
        me = int(game_state["in_action"])
        card1 = game_state["players"][me]["hole_cards"][0]
        card2 = game_state["players"][me]["hole_cards"][1]
        current_buy_in = int(game_state["current_buy_in"])
        players = game_state["players"]
        mybet = int(players["in_action"]["bet"])
        minimum_raise = int(game_state["minimum_raise"])
        call = current_buy_in-mybet
        community_cards = game_state["community_cards"]
        raise_minimum = current_buy_in - mybet + minimum_raise


        if card1["rank"] == card2["rank"] and len(game_state["community_cards"]) == 0:
            return call
        elif card1["rank"] == card2["rank"] or self.check_card_rank_in_community_cards(card1,community_cards) or self.check_card_rank_in_community_cards(card2,community_cards):
            return raise_minimum
        else:
            return 0

    def showdown(self, game_state):
        pass

    def check_card_rank_in_community_cards(self,card,community_cards):
        for com_card in community_cards:
            if com_card["rank"] == card["rank"]:
                return True
        return False
