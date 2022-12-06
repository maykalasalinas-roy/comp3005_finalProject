import sqlite3

conn = sqlite3.connect("bookstore.db")

c = conn.cursor()

def loadBook():
    file = open("bookData.txt", "r")
    lines = file.readlines()
    file.close()

    count = 0
    for line in lines:
        count += 1
        line = line.strip()
        l = line.split("\t")
        lines[count-1] = l 

    c.executemany('''INSERT INTO Book VALUES(?, ?, ?, ?, ?, ?, ?);''', lines)
    conn.commit()

    c.execute("SELECT * FROM Book")
    for n in c.fetchall():
        print(f"{n[0]}\t{n[1]}\t{n[2]}\t{n[3]}\t{n[4]}\t{n[5]}\t{n[6]}")

def loadPublisher():
    file = open("publisherData.txt", "r")
    lines = file.readlines()
    file.close()

    count = 0
    for line in lines:
        count += 1
        line = line.strip()
        l = line.split("\t")
        lines[count-1] = l 

    c.executemany('''INSERT INTO Publisher VALUES(?, ?, ?, ?, ?);''', lines)
    conn.commit()

    c.execute("SELECT * FROM Publisher")
    for n in c.fetchall():
        print(f"{n[0]}\t{n[1]}\t{n[2]}\t{n[3]}\t{n[4]}")

def loadGenre():
    file = open("genreData.txt", "r")
    lines = file.readlines()
    file.close()

    count = 0
    for line in lines:
        count += 1
        line = line.strip()
        l = line.split("\t")
        lines[count-1] = l 

    c.executemany('''INSERT INTO genre VALUES(?, ?);''', lines)
    conn.commit()

    c.execute("SELECT * FROM genre")
    for n in c.fetchall():
        print(f"{n[0]}\t{n[1]}")

def loadPhones():
    file = open("phonesData.txt", "r")
    lines = file.readlines()
    file.close()

    count = 0
    for line in lines:
        count += 1
        line = line.strip()
        l = line.split("\t")
        lines[count-1] = l 

    c.executemany('''INSERT INTO phones VALUES(?, ?);''', lines)
    conn.commit()

    c.execute("SELECT * FROM phones")
    for n in c.fetchall():
        print(f"{n[0]}\t{n[1]}")

def loadAuthor():
    file = open("authorData.txt", "r")
    lines = file.readlines()
    file.close()

    count = 0
    for line in lines:
        count += 1
        line = line.strip()
        l = line.split("\t")
        lines[count-1] = l 

    c.executemany('''INSERT INTO Author VALUES(?, ?);''', lines)
    conn.commit()

    c.execute("SELECT * FROM Author")
    for n in c.fetchall():
        print(f"{n[0]}\t{n[1]}")

def loadWrote():
    file = open("wroteData.txt", "r")
    lines = file.readlines()
    file.close()

    count = 0
    for line in lines:
        count += 1
        line = line.strip()
        l = line.split("\t")
        lines[count-1] = l 

    c.executemany('''INSERT INTO wrote VALUES(?, ?, ?);''', lines)
    conn.commit()

    c.execute("SELECT * FROM wrote")
    for n in c.fetchall():
        print(f"{n[0]}\t{n[1]}\t{n[2]}")

def loadUser():
    file = open("userData.txt", "r")
    lines = file.readlines()
    file.close()

    count = 0
    for line in lines:
        count += 1
        line = line.strip()
        l = line.split("\t")
        lines[count-1] = l 

    c.executemany('''INSERT INTO Registered_user VALUES(?, ?, ?, ?, ?);''', lines)
    conn.commit()

    c.execute("SELECT * FROM Registered_user")
    for n in c.fetchall():
        print(f"{n[0]}\t{n[1]}\t{n[2]}\t{n[3]}\t{n[4]}")


loadBook()
loadPublisher()
loadGenre()
loadPhones()
loadAuthor()
loadWrote()
loadUser()


c.close()
conn.close()