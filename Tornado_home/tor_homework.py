import json
import tornado.ioloop
from collections import defaultdict
import tornado.web
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model4 import Shops, Items, Departments

engine = create_engine('sqlite:///new_file', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class ShopHandler(tornado.web.RequestHandler):
    def get(self):
        data = session.query(Shops).all()
        return self.render('Shop_page.html', title="My title", shops=data)


class ItemsHandler(tornado.web.RequestHandler):

    def get(self, shop_id):
        data1 = session.query(Departments, Items).join(
            Items).filter(Departments.shop_id == shop_id).all()
        data = defaultdict(list)
        for dep, item in data1:
            data[dep].append(item)
        return self.render('Items.html', department=data, shop_id=shop_id)


class NewItemHandler(tornado.web.RequestHandler):
    def post(self, shop_id):
        data = json.loads(self.request.body)
        name_item = data['item_name']
        descr_item = data['item_descr']
        price_item = data['item_price']
        dep = session.query(Departments.id).filter(
            Departments.shop_id == shop_id).order_by(Departments.sphere).first()
        new_item = Items(
            name=name_item,
            description=descr_item,
            price=price_item,
            department_id=dep[0]
        )
        session.add(new_item)
        session.commit()


class APIHandler(tornado.web.RequestHandler):
    def get(self):
        data = session.query(
            Items.name, Items.description, Items.price,
            Departments.sphere, Shops.name).select_from(
            Items).join(Departments).join(Shops).all()
        result = []
        for item in data:
            dct = {
                'name': item[0],
                'description': item[1],
                'price': item[2],
                'department_name': item[3],
                'shop_name': item[4]
            }
            result.append(dct)
        return json.dumps(result)


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", ShopHandler),
        (r"/shop/(\d+)/", ItemsHandler),
        (r"/shop/(\d+)/add/", NewItemHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
