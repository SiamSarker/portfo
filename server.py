from flask import Flask, render_template, url_for, request, redirect
import csv
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route('/')
def hello_home():
    return render_template('index.html')


@app.route('/view_data')
def view_data():
    with open('database.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return '<br>'.join([', '.join(row) for row in data])

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open(os.path.join(BASE_DIR, 'database.txt'), 'a', newline='') as database:
        database.write(f"{data['email']}, {data['subject']}, {data['message']}\n")

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['email'], data['subject'], data['message']])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    return 'Something went wrong. Try again!'


if __name__ == '__main__':
    app.run(debug=True)

