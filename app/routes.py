from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, SearchForm
from app.models import User, Post, Book
from datetime import datetime
import app.api as api
import app.nyt_api as nyt_api
import ast


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    nyt_books = nyt_api.get_nyt_bestsellers()

    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('your post is now live!')
        return redirect(url_for('index'))
    posts = current_user.followed_posts().all()
    return render_template("index.html", title='Home Page', form=form, posts=posts, nyt_books=nyt_books)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.timestamp.desc())
    books = user.books
    return render_template('user.html', user=user, posts=posts, books=books)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    #if form.validate_on_submit():
    #search = form.search.data
    #books = api.get_book_data(search)
    return render_template('search.html', form=form)#, books=books)

@app.route('/results')
@login_required
def search_results(search):
    search_string = search.data['search']
    results = api.get_book_data(search_string)
    if results is None:
        flash('No results returned, try again!')
        form = SearchForm()
        return render_template('search.html', form=form)
    return render_template('results.html', books=results)

@app.route('/save', methods=['POST'])
@login_required
def save():
    data = request.form['data']
    data = ast.literal_eval(data)
    # save book data to database
    b = Book(id=data.get('id'), isbn=data.get('isbn'), title=data.get('title'), author=data.get('author'),
                image_link=data.get('image_link'), image_link_small=data.get('image_link_small'),
                description=data.get('description'), owner=current_user)
    db.session.add(b)
    db.session.commit()

    return render_template('save.html', image_link=data.get('image_link'))


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))


@app.route('/explore')
@login_required
def explore():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    books = Book.query.order_by(Book.timestamp.desc()).all()
    return render_template("index.html", title='Explore', books=books)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()