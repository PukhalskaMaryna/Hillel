from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Movie {self.id}'

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    movies = Movie.query.order_by(Movie.date_created.desc()).all()
    return render_template('index.html', movies=movies)

@app.route('/add', methods=['POST'])
def add_movie():
    movie_content = request.form['content']
    if not movie_content:
        flash('Введіть назву фільма!')
        return redirect(url_for('index'))

    new_movie = Movie(content=movie_content)
    try:
        db.session.add(new_movie)
        db.session.commit()
        flash('Фільм збережено!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Помилка при додаванні фільма!', 'error')

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_movie(id):
    movie = Movie.query.get_or_404(id)
    try:
        db.session.delete(movie)
        db.session.commit()
        flash('Фільм видалено!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Помилка при видалені!', 'error')

    return redirect(url_for('index'))

@app.route('/random')
def random_movie():
    movies = Movie.query.all()
    if not movies:
        flash('Список фільмів порожній!', 'error')
        return redirect(url_for('index'))

    movie = random.choice(movies)
    all_movies = Movie.query.order_by(Movie.date_created.desc()).all()
    flash(f'Випадковий фільм: {movie.content}', 'success')
    return render_template('index.html', movies=all_movies)

@app.route('/clear_all')
def clear_all():
    try:
        db.session.query(Movie).delete()
        db.session.commit()
        flash('Список порожній!', 'success')
    except:
        db.session.rollback()
        flash('Помилка при видаленні!', 'error')

    return redirect(url_for('index'))

@app.route('/count')
def count_movies():
    count = Movie.query.count()
    flash(f'У списку {count} фільм(-ів)', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
