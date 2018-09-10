"""往数据库中循环插入大量数据"""
import mysql.connector
import random
user = '166cai'
password = 'KmT7%16#LkdiwAvG'
host = '120.132.33.199'
database = 'bn_cpiao'
port = 3306
conn = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)
cursor = conn.cursor()
count = 0
cursor.execute('')
max_id = cursor.fetchall()
auto_increment = max_id[0][0] + 1
cursor.execute('ALTER TABLE user1 AUTO_INCREMENT = %d' % auto_increment)

for i in range(100):
    code = random.sample([0, 1, 3], 1)[0]
    if count < 30:
        cursor.execute('insert into user1 (code) values (%s)' % code)
        conn.commit()
        count = count + 1
    else:
        break
conn.close()