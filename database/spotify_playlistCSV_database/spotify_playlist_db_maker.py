import csv
import sqlite3
conn=sqlite3.connect('spotify_playlist_db.sqlite')
cur=conn.cursor()
''''''
cur.executescript('''
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Uploded_date;
DROP TABLE IF EXISTS Duration;
DROP TABLE IF EXISTS Popularity;
DROP TABLE IF EXISTS Album_Release;
DROP TABLE IF EXISTS Album_Release_Date;
DROP TABLE IF EXISTS result_table_Interested_output;

CREATE TABLE Track (Track_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Track_name TEXT UNIQUE,Aritst_id INTEGER,Album_id INTEGER,Uploded_date_id INTEGER,Duration_id INTEGER,Popularity_id INTEGER,track_preview TEXT UNIQUE);
CREATE TABLE Artist (Artist_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Artist_name TEXT UNIQUE);
CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Album_name TEXT UNIQUE,Album_Image TEXT UNIQUE,Album_Release_Date_id INTEGER);
CREATE TABLE Uploded_date (Uploded_date_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Uploded_date TEXT UNIQUE);
CREATE TABLE Duration (Duration_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Duration TEXT UNIQUE);
CREATE TABLE Popularity (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Popularity_percentage TEXT UNIQUE); 
CREATE TABLE Album_Release(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Full_Date INTEGER UNIQUE); 



'''

)

try:
    fhnad=open(input("Enter the file name: "),encoding="utf-8")
except:
    fhand=open('My Album.csv',encoding="utf-8")
reader=csv.reader(fhand)
for row in reader:
    if row[1]=='Track Name'or row[3]=='Artist Name(s)'or row[5]=='Album Name'or row[8]=='Album Release Date'or row[9]=='Album Image URL'or row[12]=='Track Duration (ms)' or row[13]=='Track Preview URL' or row[15]=='Popularity' or row[18]=='Uploded_date':
        continue
    else:
        track_name=row[1]
        artist_name=row[3]
        album_name=row[5]
        album_release_date=row[8]
        Album_Image=row[9]
        track_duration=row[12]
        track_preview=row[13]
        popularity=row[15]
        uploded_date=row[18]
        #print(track_name,artist_name,album_name,album_release_date,Album_Image,track_duration,track_preview,popularity,uploded_date)

        cur.execute('''INSERT OR IGNORE INTO Artist (Artist_name) VALUES (?)''',(artist_name,))
        cur.execute('SELECT Artist_id FROM Artist WHERE Artist_name=?',(artist_name,))
        artist_id=cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album_Release(Full_Date) VALUES (?)''',(album_release_date,))
        cur.execute('SELECT id FROM Album_Release WHERE Full_Date=?',(album_release_date,))
        Album_Release_Date_id=cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album (Album_name,Album_Image,Album_Release_Date_id) VALUES (?,?,?)''',(album_name,Album_Image,Album_Release_Date_id))
        cur.execute('SELECT id FROM Album WHERE Album_name=?',(album_name,))
        album_id=cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Uploded_date (Uploded_date) VALUES (?)''',(uploded_date,))
        cur.execute('SELECT Uploded_date_id FROM Uploded_date WHERE Uploded_date=?',(uploded_date,))
        uploded_date_id=cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Duration (Duration) VALUES (?)''',(track_duration,))
        cur.execute('SELECT Duration_id FROM Duration WHERE Duration=?',(track_duration,))
        duration_id=cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Popularity (Popularity_percentage) VALUES (?)''',(popularity,))
        cur.execute('SELECT id FROM Popularity WHERE Popularity_percentage=?',(popularity,))
        popularity_id=cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Track (Track_name,Aritst_id,Album_id,Uploded_date_id,Duration_id,Popularity_id,track_preview) VALUES (?,?,?,?,?,?,?)''',(track_name,artist_id,album_id,uploded_date_id,duration_id,popularity_id,track_preview))

#pulling out sql command form SQL_Command.txt file where i have writtten a sql command to create a table nammed result_table_Interested_output like this
'''
CREATE TABLE result_table_Interested_output AS
SELECT Track.Track_name,Track.track_preview,Popularity.Popularity_percentage,Album.Album_Image,Album_Release.Full_Date
	FROM Track,Popularity,Album,Album_Release
		ON Track.Popularity_id=Popularity.id
		AND Track.Album_id=Album.id 
		AND Album.Album_Release_Date_id=Album_Release.id
		WHERE Popularity_percentage>50 
		ORDER BY Popularity_percentage DESC

I could use, cur.executescript('the text above') then commit it will do the same thing
'''
#
#and here i have commited that table to this database
fhand2=open('SQL_Command.txt')
cur.executescript(fhand2.read())
conn.commit()

		


        
