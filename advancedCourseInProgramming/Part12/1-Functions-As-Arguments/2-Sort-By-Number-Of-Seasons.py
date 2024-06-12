# solution
def sort_by_seasons(items: list):
    def number_of_seasons(show: dict):
        return show["seasons"]
    
    return sorted(items, key=number_of_seasons)

# test
if __name__ == "__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    for show in sort_by_seasons(shows):
        print(f"{show['name']} {show['seasons']} seasons")