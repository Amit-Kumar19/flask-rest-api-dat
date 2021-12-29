from flask import Flask, request, jsonify
import dat

app = Flask(__name__)


@app.route('/checkScore', methods=['POST'])
def calculate_score():
    # GloVe model from https://nlp.stanford.edu/projects/glove/
    data = request.json['words']
    unique_values = set(data)

    if len(data) < 10:
        response = {'message': 'Words less than 10'}

    elif len(unique_values) < 10:
        response = {'message': 'Duplicates in input words'}
    else:
        model = dat.Model("glove.840B.300d.txt", "words.txt")
        score = model.dat(data)
        response = {"message": f"Calculated score {score}"}

    return jsonify(response)


if __name__ == '__main__':
    app.run(threaded=True, debug=False)
