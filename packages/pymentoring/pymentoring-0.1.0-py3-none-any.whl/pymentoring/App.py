from flask import Flask, request, jsonify

from pymentoring.anagrams.anagrams import make_anagram_from_text
from pymentoring.mycollections.my_collections import get_unique_chars

app = Flask(__name__)


@app.route("/api/v1/anagrams", methods=["POST"])
def get_anagrams():
    try:
        text = extract_text(request)
        response = make_anagram_from_text(text)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route("/api/v1/collections", methods=["POST"])
def get_unique_characters():
    try:
        text = extract_text(request)
        response = get_unique_chars(text)
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


def extract_text(req):
    json = req.get_json(silent=True)
    if json is None:
        raise TypeError("Invalid JSON")

    if not req.is_json:
        raise TypeError("Missing JSON in request")

    data = req.get_json()
    if 'text' not in data or not data['text']:
        raise TypeError("Text is missing or empty")

    return data["text"]


def start(debug_flag: bool = False):
    app.run(debug=debug_flag, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    start(True)
