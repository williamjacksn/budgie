import datetime
import flask

app = flask.Flask(__name__)


def _get_dates():
    today = datetime.date.today()
    sunday = today - datetime.timedelta(days=(today.weekday() + 1) % 7)
    week = [sunday + datetime.timedelta(i) for i in range(7)]
    return today, week


@app.route('/')
def index():
    today, week = _get_dates()
    return flask.render_template('index.html', week=week, today=today)


@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if flask.request.method == 'GET':
        today, week = _get_dates()
        return flask.render_template('add_transaction.html', today=today, week=week)
    return flask.redirect(flask.url_for('index'))


def main():
    app.run('0.0.0.0')


if __name__ == '__main__':
    main()
