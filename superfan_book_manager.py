from flask import Flask, render_template
from config import Config
from forms import LoginForm

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run()
