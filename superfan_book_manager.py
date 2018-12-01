from flask import Flask, render_template, flash, redirect, url_for
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run()
