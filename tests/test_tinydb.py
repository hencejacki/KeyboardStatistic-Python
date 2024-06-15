from tinydb import TinyDB, Query

# 连接到TinyDB数据库（如果数据库不存在则会自动创建）
db = TinyDB('db.json')

# 插入数据
db.insert({'name': 'Alice', 'age': 30})
db.insert({'name': 'Bob', 'age': 25})

# 查询数据
User = Query()
result = db.search(User.name == 'Alice')
print(result)

# 更新数据
db.update({'age': 31}, User.name == 'Alice')

# 删除数据
db.remove(User.name == 'Bob')

# 关闭数据库（可选）
db.close()
