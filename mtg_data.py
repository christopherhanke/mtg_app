from tinydb import TinyDB, Query, where


db = TinyDB("db.json")
User = Query()
if db.search(where("card") == "Yavimaya, Wiege des Wachstums"):
    print("Search succesfull")
else:
    db.insert(
        {
            "card": "Yavimaya, Wiege des Wachstums", 
            "html_tag": "Yavimaya-Cradle-of-Growth", 
            "price": 10.07, 
            "best_price": 11.0
        })
if db.search(where("card") == "Nebliger Regenwald"):
    print("Search succesfull")
else:
    db.insert(
        {
            "html_tag": "Misty-Rainforest",
            "card": "Nebliger Regenwald", 
            "price": 26.29, 
            "best_price": 31.2
        })
print(db.all())

#print(db.get(User.card == "Yavimaya, Wiege des Wachstums").doc_id)
print(db.get(doc_id=2))
