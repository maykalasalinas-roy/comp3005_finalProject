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
        #print(l)
        lines[count-1] = l 

    c.executemany('''INSERT INTO Book VALUES(?, ?, ?, ?, ?, ?, ?);''', lines)
    conn.commit()

    c.execute("SELECT * FROM Book")
    for n in c.fetchall():
        print(f"{n[0]}\t{n[1]}\t{n[2]}\t{n[3]}\t{n[4]}\t{n[5]}\t{n[6]}")
    

loadBook()

c.close()
conn.close()