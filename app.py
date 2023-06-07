import psycopg2

conn = psycopg2.connect('dbname=kino_db user=postgres host=localhost port=5432 password=Orxan_666')
cur = conn.cursor() 
# cursor -melumatlari gondermek ucundu 
# connection ise -hemin o kodlari heyata kecirmek ucundur

# query = """
# CREATE TABLE movie( 
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(50),
#     description TEXT,
#     view_count INT DEFAULT 0,
#     gener_id INT,
#     release DATE,
#     has_fragman BOOLEAN
# );

# """


# cur.execute(query)



data=[
    {"id":1,
     "title":"Avengers: Endgame",
     "description":"After the devastating events of Avengers: Infinity War, the universe is in ruins due to the efforts of the Mad Titan, Thanos.",
     "view_count":12854,
     "gener_id":1,
     "release":"2019-04-26",
     "has_fragman":True},
    {"id":2,"title":"Joker",
    "description":"In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society. He then embarks on a downward spiral of revolution and bloody crime.",
    "view_count":9652,
    "gener_id":3,
    "release":"2019-10-04",
    "has_fragman":True},
    {"id":3,"title":"Frozen II",
    "description":"Elsa, Anna, Kristoff and Olaf head far into the forest to learn the truth about an ancient mystery of their kingdom.",
    "view_count":7532,
    "gener_id":2,
    "release":"2019-11-22",
    "has_fragman":False},
    {"id":4,"title":"The Lion King",
    "description":"After the murder of his father, a young lion prince flees his kingdom only to learn the True meaning of responsibility and bravery.",
    "view_count":12598,
    "gener_id":2,
    "release":"2019-07-19",
    "has_fragman":False},
];



query="""
INSERT INTO movie(title,description,view_count,gener_id,release,has_fragman)
VALUES (%s,%s,%s,%s,%s,%s)

"""

for info in data:
    cur.execute(query,(info['title'][:8],info['description'][:10],info['view_count'],info['gener_id'],info['release'],info['has_fragman']))


# cur.execute("SELECT * FROM movie WHERE release < '2019-05-15'")

# print(cur.fetchone())


conn.commit()





 

 