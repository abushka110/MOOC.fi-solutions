# solution
class Series:
    def __init__(self, title: str, seasons_count: int, genre_list: list):
        self.title = title
        self.seasons_count = seasons_count
        self.genre_list = genre_list
        self.series_rate = []
    
    def rate(self, rating: int):
        self.series_rate.append(rating)

    def __str__(self):
        genres_string = "genres: " +", ".join(self.genre_list)
        
        if len(self.series_rate) == 0:
            return f"{self.title} ({self.seasons_count} seasons)\n" + genres_string + "\n" + f"no ratings"
        else:
            rate_points = sum(self.series_rate) / len(self.series_rate)
            return f"{self.title} ({self.seasons_count} seasons)\n" + genres_string + "\n" + f"{len(self.series_rate)} ratings, average {rate_points:.1f} points"
        
def minimum_grade(rating: float, series_list: list):
    found_series = []
    for series in series_list:
        if sum(series.series_rate) >= rating:
            found_series.append(series)
    
    return found_series

def includes_genre(genre: str, series_list: list):
    found_series = []
    for series in series_list:
        if genre in series.genre_list:
            found_series.append(series)
    
    return found_series


# test
if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)