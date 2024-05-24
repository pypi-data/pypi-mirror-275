import os
from pathlib import *
from flask import Flask, jsonify, render_template, request
from jinja2 import TemplateNotFound

def create_index_html():
    html_content = """
    <!DOCTYPE html>
    <html lang='EN'>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>FlaskApplication</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">
        <title>Flask App</title>
        <script src="{{ url_for('static', filename='js/script.js') }}"></script>
    </head>
    <body>
        <form id="myForm">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <input type="submit" value="Submit">
        </form>
        <p id="result"></p>
        <!-- rest of your HTML code -->
    </body>
    </html>
    """
    new_directory = 'templates'
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    with open(os.path.join('templates', 'index.html'), 'w') as f:
        f.write(html_content)

def create_script_js():
    js_content = """
    $(document).ready(function(){
        $('#myForm').on('submit', function(e){
            e.preventDefault();
            $.ajax({
                url : '/process',
                type : 'POST',
                data : $('#myForm').serialize(),
                success : function(response){
                    $('#result').html(response.result);
                }
            });
        });
    });
    """
    new_dir = 'static'
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    with open(os.path.join('static', 'script.js'), 'w') as f:
        f.write(js_content)

def create_app():
    app = Flask(__name__)

    @app.route('/', defaults={'path':""})
    @app.route('/<path:path>')
    def catch_all(path):
        try:
            if path=='':
                return render_template('home.html')
            return render_template(f'{path}.html')
        except TemplateNotFound:
            return render_template('index.html')

    @app.route('/process', methods=['POST'])
    def process():
        name = request.form['name']
        return jsonify({'result': 'Hello, ' + name + '!'})

    create_index_html()
    create_script_js()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=8008, debug=True)
