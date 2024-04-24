# solution
class Series:
    def __init__(self, name: str, seasons_count: int, genre_list: list):
        self.name = name
        self.seasons_count = seasons_count
        self.genre_list = genre_list

    def __str__(self):
        genres_string = "genres: " +", ".join(self.genre_list)
        
        return f"{self.name} ({self.seasons_count} seasons)\n" + genres_string + "\n" + f"no ratings"
# test
if __name__ == "__main__":
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    print(dexter)