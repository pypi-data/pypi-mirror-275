
def application():

        from flask import Flask, render_template, request, jsonify

        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template('index.html').absolute()

        @app.route('/process', methods=['POST'])
        def process():
            name = request.form['name']
            return jsonify({'result': 'Hello, ' + name + '!'})

        if __name__ == '__main__':
            app.run(host="127.0.1.0", port=8008, debug=True)

        return (application)