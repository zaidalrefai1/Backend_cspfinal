from flask import Flask, request, jsonify
from game.logic import generate_lab_level, record_result
from game.models import DifficultyModel

app = Flask(__name__)
model = DifficultyModel()

@app.route('/lab/level', methods=['GET'])
def get_lab_level():
    level = int(request.args.get('level', 1))
    level_data = generate_lab_level(level, model.extra())
    return jsonify(level_data)

@app.route('/lab/submit', methods=['POST'])
def submit_level():
    data = request.json
    correct = data.get("correct", False)
    level = data.get("level", 1)
    model.record(correct)
    return jsonify({"nextLevel": level + 1 if correct else max(1, level - 1)})

if __name__ == "__main__":
    app.run(debug=True)
