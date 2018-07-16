import json
import tornado.ioloop
import tornado.web
import sqlite3


class MainHandler(tornado.web.RequestHandler):
    conn = sqlite3.connect('db_tornado')
    cursor = conn.cursor()

    def get(self):
        students = self.cursor.execute("""select name, mark from student""").fetchall()
        result = {row[0]: row[1] for row in students}
        self.write(json.dumps(result))

    def post(self):
        data = json.loads(self.request.body)
        name = data['name']
        mark = data['mark']
        self.cursor.execute("""Insert into student(name, mark)
        values ('{}',{});""".format(name, mark))
        self.conn.commit()


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
