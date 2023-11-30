from flask import Flask, render_template, g
import psycopg2

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "default-workgroup.721630359816.us-east-1.redshift-serverless.amazonaws.com",
    "port": 5439,
    "database": "dev",
    "user": "admin",
    "password": "Redshift-pwd#1",
}


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(**db_config)
    return g.db


@app.route('/')
def index():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM sales.sales_data")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html')


@app.route('/overview')
def overview():
    return render_template('overview.html')


@app.route('/datadisplay')
def datadisplay():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM sales.sales_data LIMIT 100")
    data = cursor.fetchall()
    print(data)
    return render_template('datadisplay.html', data=data)


@app.route('/piechart')
def piechart():
    return render_template('piechart.html')


@app.route('/barchart')
def barchart():
    return render_template('barchart.html')


if __name__ == '__main__':
    app.run(debug=True)
