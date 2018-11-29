from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alexis'}
    posts = [
        {
            'author': {'username': 'Mason'},
            'body': 'I loved the Harry Potter series!'
        },
        {
            'author': {'username': 'Anders'},
            'body': 'I also thought Harry Potter series was awesome!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


if __name__ == '__main__':
    app.run()
