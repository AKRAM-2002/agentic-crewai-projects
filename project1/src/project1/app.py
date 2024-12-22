from flask import Flask, jsonify, request
from crew import Project1

app = Flask(__name__)
project = Project1()

@app.route('/generate', methods=['POST'])
def generate_jokes():
    try:
        jokes = project.generate_joke_task().run()
        if not jokes:
            return jsonify({"error": "No jokes generated."}), 400
        return jsonify({"jokes": jokes})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pick', methods=['POST'])
def pick_joke():
    try:
        jokes = request.json.get('jokes', [])
        if not jokes:
            return jsonify({"error": "No jokes provided."}), 400
        best_joke = project.pick_joke_task().run(jokes)
        return jsonify({"best_joke": best_joke})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
