import datetime
from tinydb import TinyDB, Query, where


class Database():
    """
    Database model
    """

    db = TinyDB("db.json", sort_keys=True, indent=4, separators=(",", ": "))
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
                    "price": [price],
                    "best_price": [best_price],
                    "date": [str(datetime.date.today())]
                }
            )

    def update_card(self, name, price, best_price):
        """
        update card in database\n
        """
        cards = self.db.search(where("card") == name)
        if len(cards) > 0:
            card = cards[0]
        else:
            print(f"Card ({name}) not found.")
            raise Exception

        # check if there is already a value for today, if not write new value
        if not str(datetime.date.today()) in card.get("date"):
            print("Datetime is not in list")
            # get list values from list
            card_price = card.get("price")
            card_best_price = card.get("best_price")
            card_date = card.get("date")

            # append to list new value
            card_price.append(price)
            card_best_price.append(best_price)
            card_date.append(str(datetime.date.today()))

            # update database with new lists
            self.db.update(
                {"price": card_price, "best_price": card_best_price, "date": card_date},
                where("card") == name
            )


# control execution
if __name__ == "__main__":
    db = Database()
    
    # Reset to database / uncomment next block if necessary
    # db.db.truncate()
    # db.set_card("Yavimaya, Wiege des Wachstums", "Yavimaya-Cradle-of-Growth", 10.56, 10.0)
    # db.set_card("Nebliger Regenwald", "Misty-Rainforest", 28.74, 30.5)
    
    print(db.get_cards())
    # db.update_card("Yavimaya, Wiege des Wachstums", 10.56, 10.00)
    print(db.db.get(doc_id=1))
    one_card = db.db.get(doc_id=1)
    one_date = one_card.get("date")
    print(datetime.datetime.strptime(one_date[0], "%Y-%m-%d"))
    print(datetime.datetime.now())
    one_date = one_date[0].split("-")
    for i in range(len(one_date)):
        one_date[i] = int(one_date[i])
    print(datetime.date(one_date[0], one_date[1], one_date[2]))
    
    
