"""
NMEA-0183 is a general standard for the presentation of navigation data in text format.

$GPGGA,112404.00,6003.1071858,N,03017.8198064,E,1,17,0.7,23.025,M,15.996,M,,*53

$GPGGA - type of data NMEA
112404.00 - time (hhmmss.ss)
6003.1071858 - latitude
N - latitude direction
03017.8198064 - longitude
E - direction of longitude
"""

"""
Base: Lat: 60.051584° Lon: 30.300509°
"""
from math import *


def timeoutdistbetween(koorddict, base, dist, gap):
    r_met = 6371007
    time = 0
    lat0 = radians(base[0])
    lon0 = radians(base[1])
    for key in koorddict.keys():
        d_lat = radians(koorddict[key][0]) - lat0
        d_lon = radians(koorddict[key][1]) - lon0

        lat_norm = cos((radians(koorddict[key][0]) + lat0) / 2)
        meters = r_met * hypot(d_lon * lat_norm, d_lat)
        if meters <= dist:
            time += gap
    return time

def reformdata(i):
    deg = int(i // 100)
    mins = int(i % 100)
    secs = i % 1 * 60
    wrtype = deg + mins / 60 + secs / 3600
    return wrtype


def read_data(filename):
    koorddict = {}
    file = open(filename, "r")
    for line in file:
        string = (line.split(','))
        try:
            if string[3] == "S":
                string[2] *= -1

            if string[5] == "W":
                string[4] *= -1

            koorddict[float(string[1])] = [reformdata(float(string[2])), reformdata(float(string[4]))]
        except:
            pass

    file.close()
    return koorddict


def timetransform(time):
    s = time % 60
    m = time // 60
    h = time // 3600
    return h, m, s


def main():
    basecoord = [60.051584, 30.300509]
    dist_limit = 25
    fileName = "nmea.log"
    # fileName = input("Enter file name, please: ")
    gap = 0.2
    koorddict = read_data(fileName)
    timefarfrom = timeoutdistbetween(koorddict, basecoord, dist_limit, gap)
    h, m, s = timetransform(int(timefarfrom))
    print(f"Аппарат был на расстоянии менее чем 25 метров от точки"
          f" с координатами: Lat: {basecoord[0]} Lon: {basecoord[1]} \nhour-{h:.0f} min-{m:02.0f} sec-{s:02.0f}")


if __name__ == '__main__':
    main()
