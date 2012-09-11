import os
import psycopg2
from random import choice

conn = psycopg2.connect("host=domain dbname=databasename user=username password=** port=5432")
cur = conn.cursor()
path = "C:/Users/Wouter/Desktop/wallpapers/"

with open("dates.txt") as f:
		dates = f.readlines()

with open("names.txt") as f:
		names = f.readlines()

for wallpaper in os.listdir(path):
	id = wallpaper.rsplit("-")[1]
	id = int(id.rsplit(".")[0])
	landscape = True
	created_on = choice(dates).strip()

	cur.execute("INSERT INTO wallpapers (id, filename, landscape, created_on) VALUES (%s, %s, %s, %s)", (id, wallpaper, landscape, created_on))

conn.commit()
cur.close()
conn.close()