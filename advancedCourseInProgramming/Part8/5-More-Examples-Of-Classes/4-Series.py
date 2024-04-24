# solution
class Series:
    def __init__(self, name: str, seasons_count: int, genre_list: list):
        self.name = name
        self.seasons_count = seasons_count
        self.genre_list = genre_list
        self.series_rate = []
    
    def rate(self, rating: int):
        self.series_rate.append(rating)

    def __str__(self):
        genres_string = "genres: " +", ".join(self.genre_list)
        
        if len(self.series_rate) == 0:
            return f"{self.name} ({self.seasons_count} seasons)\n" + genres_string + "\n" + f"no ratings"
        else:
            rate_points = sum(self.series_rate) / len(self.series_rate)
            return f"{self.name} ({self.seasons_count} seasons)\n" + genres_string + "\n" + f"{len(self.series_rate)} ratings, average {rate_points:.1f} points"
# test
if __name__ == "__main__":
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)