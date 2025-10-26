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

def githubCopilotTest():
    """
    This function is a placeholder to test the functionality of the github copilot AI.
    It simply renders the index.html template and returns the resulting HTML.
    """
    return render_template('index.html')

def write_to_file(data):
    """
    Writes the given data to the database.txt file in the format email, subject, message.
    That's the trick
    """
    if data is None:
        raise ValueError("Data cannot be None")
    try:
        with open(os.path.join(BASE_DIR, 'database.txt'), 'a', newline='') as database:
            if database is None:
                raise IOError("Database file cannot be opened")
            database.write(f"{data['email']}, {data['subject']}, {data['message']}\n")
    except IOError as e:
        print(f"IOError: {e}")
        raise
    except KeyError as e:
        print(f"KeyError: {e}")
        raise

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

