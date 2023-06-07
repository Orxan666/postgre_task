import psycopg2

conn=psycopg2.connect('dbname=movie_db user=postgres host=localhost port=5432 password=Orxan_666') 
cur=conn.cursor()


# query="""
# CREATE TABLE movie(
# id SERIAL PRIMARY KEY,
# title VARCHAR(50),
# description TEXT,
# view_count INT DEFAULT 0,
# gener_id INT,
# release DATE,
# has_fragman BOOLEAN
# );
# """
# cur.execute(query)

data=[
  {
    "id": 1,
    "title": "The Avengers",
    "description": "Earth's mightiest heroes must come together to fight against a powerful enemy.",
    "view_count": 1200,  
    "gener_id": 3,
    "release": "2012-05-04",
    "has_fragman": True
  },
  {
    "id": 2,
    "title": "Inception",
    "description": "A skilled thief enters people's dreams to steal valuable information.",
    "view_count": 980,
    "gener_id": 5,
    "release": "2010-07-16",
    "has_fragman": True
  },
  {
    "id": 3,
    "title": "The Shawshank Redemption",
    "description": "Two imprisoned men forge a deep bond over several years.",
    "view_count": 1500,
    "gener_id": 1,
    "release": "1994-09-23",
    "has_fragman": False
  },
  {
    "id": 4,
    "title": "The Dark Knight",
    "description": "Batman sets out to dismantle the remaining criminal organizations that plague Gotham City.",
    "view_count": 2000,
    "gener_id": 3,
    "release": "2008-07-18",
    "has_fragman": True
  },
  {
    "id": 5,
    "title": "Pulp Fiction",
    "description": "Various stories intertwine in the criminal underworld of Los Angeles.",
    "view_count": 1750,
    "gener_id": 2,
    "release": "1994-10-14",
    "has_fragman": False
  },
  {
    "id": 6,
    "title": "Interstellar",
    "description": "A group of explorers travel through a wormhole in search of a new habitable planet.",
    "view_count": 900,
    "gener_id": 5,
    "release": "2014-11-07",
    "has_fragman": True
  },
  {
    "id": 7,
    "title": "Forrest Gump",
    "description": "A simple-minded but kind-hearted man witnesses and unwittingly influences several defining historical events in the 20th century USA.",
    "view_count": 1320,
    "gener_id": 4,
    "release": "1994-07-06",
    "has_fragman": False
  },
  {
    "id": 8,
    "title": "Fight Club",
    "description": "An insomniac office worker forms an underground fight club as a form of therapy.",
    "view_count": 1120,
    "gener_id": 2,
    "release": "1999-10-15",
    "has_fragman": True
  },
  {
    "id": 9,
    "title": "The Matrix",
    "description": "A computer hacker learns about the True nature of his reality and his role in the war against the machines.",
    "view_count": 1850,
    "gener_id": 5,
    "release": "1999-03-31",
    "has_fragman": False
  },


]

query="""
INSERT INTO movie(title,description,view_count,gener_id,release,has_fragman)
VALUES (%s,%s,%s,%s,%s,%s)

"""

for info in data:
    cur.execute(query,(info['title'][:5],info['description'][:8],info['view_count'],info['gener_id'],info['release'],info['has_fragman']))

cur.execute("SELECT MIN(view_count) FROM movie")
print(cur.fetchall())
conn.commit()


