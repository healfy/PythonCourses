from flask import Flask, render_template, request, jsonify,redirect
from model4 import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from collections import defaultdict


app = Flask(__name__)
engine = create_engine('sqlite:///new_file', echo=False)
Base = declarative_base()


@app.route('/', methods=['GET'])
def shops():
    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(Shops).all()
    return render_template('Main_page.html', shops=data)


@app.route('/shop/<shop_id>/', methods=['GET'])
def department(shop_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    data1 = session.query(Departments, Items).join(
        Items).filter(Departments.shop_id == shop_id).all()
    data = defaultdict(list)

    for dep, item in data1:
        data[dep].append(item)
    return render_template('second_page.html', department=data, shop_id=shop_id)


@app.route('/shop/<shop_id>/add/', methods=['GET', 'POST'])
def post(shop_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    if request.method == 'POST':
        name_item = request.form['item_name']
        descr_item = request.form['item_descr']
        price_item = request.form['item_price']
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
        return redirect('/shop/{}/'.format(shop_id))

    else:
        return render_template('post.html')


@app.route('/api/items/', methods=['GET'])
def api():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = []
    data = session.query(
        Items.name, Items.description, Items.price,
        Departments.sphere, Shops.name).select_from(
        Items).join(Departments).join(Shops).all()
    for item in data:
        dct = {
            'name': item[0],
            'description': item[1],
            'price': item[2],
            'department_name': item[3],
            'shop_name': item[4]
        }
        result.append(dct)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
