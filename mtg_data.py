from tinydb import TinyDB, Query, where


class Database():
    """
    Database model
    """

    db = TinyDB("db.json")
    c_query = Query()

    def get_cards(self):
        """returns list of cards in database"""
        cards = []
        for item in self.db:
            cards.append(item["card"])
        
        return cards

    def get_card(self, name):
        """
        get card out of database by name\n
        returns item from database or None
        """
        items = self.db.search(self.c_query.card == name)
        if len(items) > 0:
            return items[0]
        else:
            return None

    def set_card(self, name, html_tag, price, best_price):
        """
        set card in database\n
        """
        # check if card is yet in database, if then update
        if name in self.get_cards():
            self.update_card(name, price, best_price)
        
        # if card is not yet in database insert it
        else:
            self.db.insert(
                {
                    "card": name,
                    "html_tag": html_tag,
                    "price": price,
                    "best_price": best_price
                }
            )

    def update_card(self, name, price, best_price):
        """
        update card in database\n
        """
        # self.db.update({"price": price, "best_price": best_price}, self.c_query.card == name)
        self.db.update({"price": price, "best_price": best_price}, where("card") == name)
        


if __name__ == "__main__":
    db = Database()
    print(db.get_cards())
    db.update_card("Yavimaya, Wiege des Wachstums", 10.56, 10.00)
    print(db.db.get(doc_id=1))

# if db.search(where("card") == "Yavimaya, Wiege des Wachstums"):
#     print("Search succesfull")
# else:
#     db.insert(
#         {
#             "card": "Yavimaya, Wiege des Wachstums", 
#             "html_tag": "Yavimaya-Cradle-of-Growth", 
#             "price": 10.07, 
#             "best_price": 11.0
#         })
# if db.search(Card.card == "Nebliger Regenwald"):
#     print("Search succesfull")
# else:
#     db.insert(
#         {
#             "html_tag": "Misty-Rainforest",
#             "card": "Nebliger Regenwald", 
#             "price": 26.29, 
#             "best_price": 31.2
#         })
# db.update({"price": 0}, Card.card == "Nebliger Regenwald")
# print(db.get(Card.card == "Yavimaya, Wiege des Wachstums").doc_id)
# print(db.get(doc_id=2))
# print(db.search(Card.card == "Nebliger Regenwald"))
# for item in db:
#     print(item["card"])
