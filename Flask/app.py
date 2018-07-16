from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Привет! :)'


@app.route('/bye/')
def bye():
    return 'Пока! :('


@app.route('/students/')
def students():
    all_students = {
        'Алекс': 9,
        'Джон': 5,
        'Иван': 10,
        'Сигизмунд': 7}
    return render_template('student.html', students=all_students)


if __name__ == '__main__':
    app.run()
