import sqlite3
import random
import time
import string
import os




db = sqlite3.connect("c:/Users/Aleksi/Documents/koulu/ohjelmointi/kannat/test.db")
db.isolation_level = None
try:
    db.execute("CREATE TABLE Elokuvat (id INTEGER PRIMARY KEY, nimi TEXT, vuosi INTEGER)")
except:
    print("database already found")
db.execute("Delete from elokuvat")    
if db.execute("Select Count(id) From Elokuvat").fetchone()[0] == 0:
    start = time.time()
    db.execute("BEGIN;")
    for x in range(1000000):
        letters = string.ascii_lowercase
        nimi= ''.join(random.choice(letters) for i in range(8)) 
        db.execute("INSERT INTO Elokuvat (nimi, vuosi) VALUES (?,?)", [nimi,random.randint(1900,2000)])
    db.execute("COMMIT;")
    end = time.time()
    print("testi 1 rakennus aika", end - start)
    start = time.time()
    db.execute("BEGIN;")
    for x in range(1000):
        db.execute("Select Count(vuosi) From Elokuvat E Where vuosi=?", [random.randint(1900,2000)])
    db.execute("COMMIT;")
    end = time.time()
    print("testi 1 kyselyt aika", end - start)
    b = os.path.getsize("c:/Users/Aleksi/Documents/koulu/ohjelmointi/kannat/test.db")
    print(b)
db.execute("Delete from elokuvat")
if db.execute("Select Count(id) From Elokuvat").fetchone()[0] == 0:
    print("Database successfully emptied")
else:
    print("Error after test1")



try:
    db.execute("CREATE TABLE Elokuvat (id INTEGER PRIMARY KEY, nimi TEXT, vuosi INTEGER)")
except:
    print("database already found")
if db.execute("Select Count(id) From Elokuvat").fetchone()[0] == 0:
    start = time.time()
    db.execute("CREATE INDEX idx_test ON Elokuvat (vuosi);")
    db.execute("BEGIN;")
    for x in range(1000000):
        letters = string.ascii_lowercase
        nimi= ''.join(random.choice(letters) for i in range(8))             
        db.execute("INSERT INTO Elokuvat (nimi, vuosi) VALUES (?,?)", [nimi,random.randint(1900,2000)])
    db.execute("COMMIT;")
    end = time.time()
    print("testi 2 rakennus aika", end - start)
    start = time.time()
    db.execute("BEGIN;")
    for x in range(1000):
        db.execute("Select Count(vuosi) From Elokuvat E Where vuosi=?", [random.randint(1900,2000)])
    db.execute("COMMIT;")
    end = time.time()
    print("testi 2 kyselyt aika", end - start)
    b = os.path.getsize("c:/Users/Aleksi/Documents/koulu/ohjelmointi/kannat/test2.db")
    print(b)
db.execute("Delete from elokuvat")
if db.execute("Select Count(id) From Elokuvat").fetchone()[0] == 0:
    print("Database successfully emptied")
else:
    print("Error after test 2")



db = sqlite3.connect("c:/Users/Aleksi/Documents/koulu/ohjelmointi/kannat/test3.db")
db.isolation_level = None
try:
    db.execute("CREATE TABLE Elokuvat (id INTEGER PRIMARY KEY, nimi TEXT, vuosi INTEGER)")
except:
    print("database already found")
if db.execute("Select Count(id) From Elokuvat").fetchone()[0] == 0:
    start = time.time()
    db.execute("BEGIN;")
    for x in range(1000000):
        letters = string.ascii_lowercase
        nimi= ''.join(random.choice(letters) for i in range(8)) 
        db.execute("INSERT INTO Elokuvat (nimi, vuosi) VALUES (?,?)", [nimi,random.randint(1900,2000)])   
    db.execute("COMMIT;")
    db.execute("CREATE INDEX idx_test ON Elokuvat (vuosi);")  
    end = time.time()
    print("testi 3 rakennus aika", end - start)
    start = time.time()
    db.execute("BEGIN;")
    for x in range(1000):
        db.execute("Select Count(vuosi) From Elokuvat E Where vuosi=?", [random.randint(1900,2000)])
    db.execute("COMMIT;")
    end = time.time()
    print("testi 3 kyselyt aika", end - start)
    b = os.path.getsize("c:/Users/Aleksi/Documents/koulu/ohjelmointi/kannat/test3.db")
    print(b)
db.execute("Delete from elokuvat")
if db.execute("Select Count(id) From Elokuvat").fetchone()[0] == 0:
    print("Database successfully emptied")
else:
    print("Error after test 3")

