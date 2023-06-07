import psycopg2

con = psycopg2.connect('dbname=job_search_db user=postgres host=localhost port=5432 password=Orxan_666')
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



# query = """
# CREATE TABLE jobs(id SERIAL PRIMARY KEY,
#  title TEXT, gain INT, expiration_date DATE, lang BOOLEAN, city VARCHAR(50));
# """

# cur.execute(query)
# con.commit()

 

# query = """
# ALTER TABLE jobs DROP COLUMN city;
# ALTER TABLE jobs RENAME COLUMN gain TO salary;
# ALTER TABLE jobs ADD COLUMN company VARCHAR(50);
# """

# cur.execute(query)
# con.commit()


# info_list = [
#     # basliq, sirket, maas, bitme tarixi, xarici dil telebi
#     ('iOS developer', 'A2Z Technologies', 3500, '2022-07-18', True),
#     ('Tender üzrə mütəxəssis', 'A2Z Technologies', 1500, '2022-06-11', False),
#     ('Məlumat bazası üzrə inzibatçı', 'ABB ASC', 1500, '2022-07-12', True),
#     ('Database Administrator', 'A2Z Technologies', 2500, '2022-07-14', True),
#     ('Front-End Developer', 'AzəriMed QSC', 1500, '2022-07-23', False),
#     ('Proqram təminatının testləşdirilməsi üzrə mühəndis',
#      'ABB ASC', 1500, '2022-08-10', False),
#     ('Back-end üzrə proqramçı', 'ABB ASC', 4100, '2022-07-11', True),
#     ('Biznes analitika üzrə Baş mütəxəssis ', 'ABB ASC', 2200, '2022-07-03', True),
#     ('Android proqramçı', 'ABB ASC', 1300, '2022-07-22', True),
#     ('Front-end üzrə proqramçı', 'ABB ASC', 3200, '2022-07-06', True),
#     ('Full stack PHP proqramçı', 'AzəriMed QSC', 2400, '2022-07-17', False),
#     ('Avtomatlaşdırılmış əməliyyat sistemi üzrə proqramçı',
#      'ABB ASC', 2700, '2022-07-15', True),  
#     ('Proqram təminatı üzrə mühəndis', 'Kontakt Home', 2700, '2022-07-13', False),
#     ('Hüquqşünas', 'Kontakt Home', 1500, '2022-07-03', False),
#     ('Çatdırılma xidmətləri üzrə fəhlə', 'Kontakt Home', 500, '2022-07-15', True),
#     ('PHP developer', 'ARIS', 1500, '2022-07-11', True),
#     ('Məhsul üzrə menecer', 'Kontakt Home', 2800, '2022-07-05', True),
#     ('Proqram təminatı üzrə aparıcı mühəndis',
#      'Kontakt Home', 2500, '2022-07-02', False),
#     ('İT sənədləşməsi üzrə mütəxəssis', 'Azericard', 1500, '2022-07-25', True),
#     ('Information Security Specialist', 'DEFSCOPE LLC', 2500, '2022-07-03', False),
#     ('IT Helpdesk', 'Azericard', 1500, '2022-07-30', True),
#     ('Cybersecurity Business Development Internship',
#      'DEFSCOPE LLC', 2900, '2022-07-19', False),
#     ('Vue.js developer', 'ARIS', 1500, '2022-07-29', True),
# ]

# query="""
# INSERT INTO jobs (title, company, salary, expiration_date, lang) VALUES (%s, %s, %s, %s, %s)
# """
# for i in info_list:
#     cur.execute(query,i)

# # con.commit()
# query="SELECT * FROM jobs"
# cur.execute(query)
# show(cur)

# query="SELECT * FROM jobs WHERE company='ABB ASC'"

# query="SELECT * FROM jobs WHERE company='ABB ASC' and salary<2000"

# query="SELECT * FROM jobs WHERE company='Kontakt Home' and expiration_date>'2022-07-10'"

# query="SELECT * FROM jobs WHERE lang='False' and salary>2500"

# query="SELECT * FROM jobs WHERE title LIKE '%proqramçı'"

# query="SELECT * FROM jobs WHERE NOT title LIKE '%end%'"

# query = "SELECT * FROM jobs WHERE title LIKE 'IT%' OR title LIKE 'İT%'"

# query = "SELECT * FROM jobs WHERE lang=true ORDER BY salary"

# query = "SELECT * FROM jobs WHERE salary=(SELECT MAX(salary) FROM jobs) "

# query = "SELECT * FROM jobs WHERE expiration_date>'2022-07-10' ORDER BY expiration_date OFFSET 1 LIMIT 3"

# query = "SELECT COUNT(*) FROM jobs WHERE expiration_date<'2022-07-10'"

# query = "SELECT * FROM jobs WHERE lang=false ORDER BY salary DESC LIMIT 1"

# query = "SELECT company, salary FROM jobs WHERE lang=false ORDER BY salary DESC LIMIT 1"

# query = "SELECT * FROM jobs WHERE lang=true ORDER BY salary LIMIT 1"

# query = " SELECT AVG(salary) FROM jobs WHERE title LIKE '%proqramçı%' OR title LIKE '%Proqramçı%' OR title LIKE '%developer%' OR title LIKE '%Deveroper%' "

# query = "SELECT SUM(salary) FROM jobs WHERE company='Kontakt Home' OR company='AzəriMed QSC' OR company='A2Z Technologies'"

# query = "SELECT * FROM jobs WHERE (title LIKE '%developer%' OR  title LIKE '%proqramçı%') AND lang=false"

# query = "SELECT * FROM jobs WHERE (company='Kontakt Home' OR company='AzəriMed QSC' OR company='A2Z Technologies') AND salary BETWEEN 2500 AND 3000"





# con.commit()


# query="SELECT * FROM jobs"


# import os 
# os.system('cls')


# query = """SELECT company, SUM(salary) as salary FROM jobs WHERE expiration_date > '2022-04-28' GROUP BY company HAVING AVG(salary) > 2000"""
# query = """
# SELECT
# 	SUM (salary)
# FROM
# 	jobs
# GROUP BY
# 	company;
#     """

# cur.execute(query)
# con.commit()


# query = "SELECT * FROM jobs;"
# cur.execute(query)
# show(cur)


# --------------------------------------UPDATE DELETE GROUP
# query = """UPDATE product SET brand='Coca Cola' WHERE brand='Fanta'"""
# query = """UPDATE product SET local=false WHERE brand='Coca Cola'"""
# query = """UPDATE product SET price=price*1.2 WHERE brand='Coca Cola'"""
# query = """DELETE FROM product WHERE price<1"""
# query = """UPDATE product SET price=price*1.2 WHERE brand='Coca Cola'"""
# query = """UPDATE product SET price=price*1.2 WHERE brand='Coca Cola'"""
# query = """SELECT brand, SUM(price) FROM product GROUP BY brand;"""
# query = """SELECT brand, AVG(price) as sum_price FROM product WHERE expire > '2022-04-28' GROUP BY brand HAVING AVG(price) > 1.7"""
# ------------------------------------
# LESSON 33


# 2ci sual 

# query = """UPDATE jobs SET salary=salary*1.15 WHERE salary<2000 AND expiration_date > '2022-07-10';"""
# cur.execute(query)
# con.commit()

# cur.execute('SELECT * FROM jobs')
# show(cur)

# 3-cu sual


# query= """DELETE FROM jobs WHERE title LIKE '%PHP%';"""

# cur.execute(query)
# con.commit()

# cur.execute('SELECT * FROM jobs')
# show(cur)


# 4-cu sual 



# query= """SELECT company,AVG(salary) FROM jobs GROUP BY company HAVING AVG(salary)>2000;"""
# cur.execute(query)
# show(cur)


