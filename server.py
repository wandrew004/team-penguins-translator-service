from flask import Flask
from flask import request, jsonify
from src.translator import translate_content

app = Flask(__name__)

@app.route("/")
def translator():
    content = request.args.get("content", default = "", type = str)
    is_english, translated_content = translate_content(content)
    return jsonify({
        "is_english": is_english,
        "translated_content": translated_content,
    })
