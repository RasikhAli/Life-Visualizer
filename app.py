from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    age_years = int(request.json.get('age', 0))
    unit = request.json.get('unit', 'months')
    total_units = 0

    if unit == 'months':
        total_units = age_years * 12
    elif unit == 'weeks':
        total_units = age_years * 52
    elif unit == 'days':
        total_units = age_years * 365

    life_circles = [{'id': i} for i in range(total_units)]

    return jsonify(life_circles)

if __name__ == '__main__':
    app.run(debug=True)