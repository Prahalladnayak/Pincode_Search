from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    error = None

    if request.method == 'POST':
        pincode = request.form['pincode']
        url = f"https://api.postalpincode.in/pincode/{pincode}"
        response = requests.get(url)

        if response.status_code == 200:
            result = response.json()
            if result[0]['Status'] == 'Success':
                data = result[0]['PostOffice']
            else:
                error = "Invalid Pincode entered!"
        else:
            error = "API Error. Please try again."

    return render_template('index.html', data=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
