import sqlite3

db = sqlite3.connect("c:/Users/Aleksi/Documents/koulu/ohjelmointi/kannat/bikes.db")
db.isolation_level = None
city="city5"
station = db.execute("Select S.name, Count(T.from_id) From Stops S, Bikes B, Trips T, Cities C Where C.name =? AND T.bike_id=B.id AND C.id=B.city_id AND S.id=T.from_id  Group by S.name Order by Count(T.from_id) desc", [city]).fetchone()
print( station)
#43102

def distance_of_user(user):
    matka = db.execute("Select SUM(distance) From Trips T, Users U Where U.name =? AND U.id=t.user_id", [user]).fetchone()[0]
    return matka
    

def speed_of_user(user):
    speed = round(db.execute("Select SUM(distance)*60.0/(SUM(duration)*1000) From Trips T, Users U Where U.name =? AND U.id=t.user_id", [user]).fetchone()[0],2)
    return speed


def duration_in_each_city(day):
    time = db.execute("Select C.name, SUM(T.duration) From Bikes B, Trips T, Cities C Where T.day =? AND T.bike_id=B.id AND C.id=B.city_id Group by C.name", [day]).fetchall()
    return time

def users_in_city(city):
    users = db.execute("Select Count(distinct(T.user_id)) From Bikes B, Trips T, Cities C Where C.name=? AND T.bike_id=B.id AND C.id=B.city_id", [city]).fetchone()[0]
    return users
def trips_on_each_day(city):
    trips = db.execute("Select T.day, Count(T.from_id) From Bikes B, Trips T, Cities C Where C.name=? AND T.bike_id=B.id AND C.id=B.city_id Group by T.day", [city]).fetchall()
    return (trips)
def most_popular_start(city):#ilmoittaa kaupungin suosituimman aloitusaseman matkalle sekä matkojen määrän. (4 pistettä)
    station = db.execute("Select S.name, Count(T.from_id) From Stops S, Bikes B, Trips T, Cities C Where C.name =? AND T.bike_id=B.id AND C.id=B.city_id AND S.id=T.from_id  Group by S.name Order by Count(T.from_id) desc", [city]).fetchone()
    return( station)

