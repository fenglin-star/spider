import time
from Student_project.settings import MONGO_DB

mongodb = MONGO_DB['China_StudentProjectItem']

first = 0
old_counts = 0
while True:
    now_counts = mongodb.find().count()
    add_count = now_counts - old_counts
    print(str(first) + ':    现在数据库有 '+ str(now_counts) + ' 条数据' + '  比上次增加了 ' + str(add_count) + ' 条数据')
    old_counts =  now_counts
    first = first + 1
    time.sleep(5)
