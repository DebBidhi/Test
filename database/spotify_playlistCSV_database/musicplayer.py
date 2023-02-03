import vlc
import csv
import sqlite3
conn=sqlite3.connect('spotify_playlist_db.sqlite')
cur=conn.cursor()
a=None
a=input('Enter to stop')
music_links = []
cur.execute(''' SELECT track_preview FROM Track WHERE track_preview!='' ''')
songs=cur.fetchall()
for song in songs:
    if song[0]=='' and song[0] is None and song[0]=='Null':
        continue
    music_links.append(song[0])
print(music_links)

for music_link in music_links:
    player = vlc.MediaPlayer(music_link)
    player.play()
    while player.get_state() != vlc.State.Ended:
        pass
stop=player.stop()

if a is not None:
    stop


