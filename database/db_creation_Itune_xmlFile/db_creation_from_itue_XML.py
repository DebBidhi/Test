import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;


CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)''')
try:
    fhand=open(input("enter the file name: "))
except:
    fhand=open("Library.xml")


#iterates through the children of "d" and checks if the tag of a child is "key" and 
#its text matches the specified "key". If the matching key is found, 
#the function sets the "found" flag to True and returns the text of the next child element.
#If no matching key is found, the function returns None.
def lookup(d,key):
    found=False
    for child in d:
        if found: return child.text
        if child.tag=='key' and child.text==key:
            found=True
    return None
    

stuff = ET.parse(fhand)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    Genre=lookup(entry,'Genre')

    if name is None or artist is None or album is None or Genre is None :  
        continue

    print(name, artist, album, count, rating, length, Genre)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', ( Genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (Genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count,genre_id ) VALUES ( ?, ?, ?, ?, ?,? )''', 
        ( name, album_id, length, rating, count,genre_id ) )

conn.commit()

