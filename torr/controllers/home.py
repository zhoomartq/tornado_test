
'''
Preset controller by torn for / route
'''
from .modules import *
conn=sqlite3.connect('test.db')
try:
	conn.execute('''create data)''')
except Exception:
	print('data alrady existe')
curser=conn.cursor()

class homeHandler(tornado.web.RequestHandler):
	#READ
	def get(self):
		records=curser.execute('SELECT * FROM posts')
		self.write(tornado.escape.json_encode(records.fetchall()))

	#Create
	def post(self):
		record=tornado.escape.json_decode(self.request.body)
		curser.execute("INSERT INTO posts values(:id,:title,:body)",record)
		self.get()
	
	#DELETE
	def delete(self):
		post_id=tornado.escape.json_decode(self.request.body)
		curser.execute('DELETE FROM posts WHERE id ={}'.format(post_id['id']))
		self.get()
	
	#UPDATE
	def put(self):
		record=tornado.escape.json_decode(self.request.body)
		curser.execute('UPDATE posts SET title=:title,body=:body WHERE id=:id',record)
		self.get()