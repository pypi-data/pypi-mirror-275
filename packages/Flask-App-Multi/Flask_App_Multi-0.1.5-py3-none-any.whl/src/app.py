
class Application():
        
        def __init__(self):
            self

        def application(self):

            from flask import Flask, render_template, request, jsonify
            from jinja2 import TemplateNotFound
            from pathlib import Path

            app = Flask(__name__, template_folder="/")

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

            if __name__ == '__main__':
                app.run(host="127.0.1.0", port=5005, debug=True)

            return