from flask import Flask, request, jsonify
from flask_cors import CORS
from calculations import get_growth_percentiles

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    age = float(data.get('age'))
    weight = float(data.get('weight'))
    height = float(data.get('height'))
    gender = data.get('gender')

    weight_percentile, height_percentile = get_growth_percentiles(age, weight, height, gender)

    result = {
        'age': age,
        'weight': weight,
        'height': height,
        'weightPercentile': weight_percentile,
        'heightPercentile': height_percentile
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)