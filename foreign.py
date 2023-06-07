import psycopg2

con = psycopg2.connect('dbname=blog3_db user=postgres host=localhost port=5432 password=Orxan_666')
cur = con.cursor()

def show(cursor):
    # cur.execute(query)
    length = 20
    print(*[desc[0].ljust(20) for desc in cursor.description], sep='')
    print('-'*140)
    result = cur.fetchall()
    for row in result:
        for col in row:
            print(str(col).ljust(length)[:17], end='')
        print()


query="""
CREATE TABLE author(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
CREATE TABLE tag(
    id SERIAL PRIMARY KEY,
	title VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE article(
    id SERIAL PRIMARY KEY,
	title VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    author_id INT,
    CONSTRAINT fk_author
        FOREIGN KEY(author_id)
            REFERENCES author(id)
                ON DELETE SET NULL

);

"""

cur.execute(query)
con.commit()