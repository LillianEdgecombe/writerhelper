from flask import Flask, render_template, request, jsonify, Response
from char_dev import Character
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-portrait', methods=['POST'])
def generate_portrait():
    data = request.json
    char = Character(data)
    portrait_url = char.generate_portrait_url()
    return jsonify({"portrait_url": portrait_url})

@app.route('/export-markdown', methods=['POST'])
def export_markdown():
    data = request.json
    char = Character(data)
    markdown_content = char.to_markdown()
    filename = char.get_safe_filename()

    return Response(
        markdown_content,
        mimetype="text/markdown",
        headers={"Content-disposition": f"attachment; filename={filename}"}
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
