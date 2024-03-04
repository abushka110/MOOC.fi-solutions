# solution
import math

def get_station_data(filename: str):
    data = {}
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            line = line.split(";")
            if line[0] == "Longitude":
                continue
            data[line[3]] = (round(float(line[0]), 15), round(float(line[1]), 15))
    return data

def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]
    x_as_km = (longitude1-longitude2) * 55.26
    y_as_km = (latitude1-latitude2) * 111.2
    return math.sqrt(x_as_km**2 + y_as_km**2)

def greatest_distance(stations: dict):
    greatest = 0
    for start_station in stations:
        for end_station in stations:
            e = distance(stations, start_station, end_station)
            if e > greatest:
                greatest = e
                station1 = start_station
                station2 = end_station
    return station1, station2, greatest


# test
if __name__ == "__main__":
    # test 1
    # get_station_data("stations1.csv")

    # test 2
    # stations = get_station_data('stations1.csv')
    # d = distance(stations, "Designmuseo", "Hietalahdentori")
    # print(d)
    # d = distance(stations, "Viiskulma", "Kaivopuisto")
    # print(d)

    # test 3
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)