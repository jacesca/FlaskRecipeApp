from datetime import datetime, UTC
from flask import Flask, redirect, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipe.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Emulating the database
all_recipes = [
    {'title': 'Recipe No.1', 'description': 'Some ingredients for Recipe 1',
     'author': 'Joey'},
    {'title': 'Recipe No.2', 'description': 'Some ingredients for Recipe 2'},
]


# Table definition
class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    author = db.Column(db.String(50))
    data_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.now(UTC))

    def __repr__(self):
        return f'Recipe No.{self.id}'


@app.route('/home2/')
def hellohome():
    return "Hello world!"


@app.route('/hello/<string:name>')
def hello(name):
    return f"Hello {name}!"


@app.route('/')
@app.route('/home/')
def home():
    num_recipes = Recipe.query.count()
    return render_template('index.html', num_recipes=num_recipes)


@app.route('/recipes_dict')
def recipes_dict():
    return render_template('recipes_dict.html', recipes=all_recipes)


@app.route('/list_recipes', methods=['GET', 'POST'])
def recipes_all_together():
    if request.method == 'POST':
        recipe_title = request.form['title']
        recipe_description = request.form['description']
        recipe_author = request.form['author']
        new_recipe = Recipe(title=recipe_title, description=recipe_description,
                            author=recipe_author)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect('/list_recipes')
    else:
        all_recipes = Recipe.query.all()
        return render_template('list_recipes.html', recipes=all_recipes)


@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    all_recipes = Recipe.query.all()
    return render_template('recipes.html', recipes=all_recipes)


@app.route('/recipes/new', methods=['GET', 'POST'])
def new_recipe():
    if request.method == 'POST':
        recipe_title = request.form['title']
        recipe_description = request.form['description']
        recipe_author = request.form['author']
        new_recipe = Recipe(title=recipe_title, description=recipe_description,
                            author=recipe_author)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect('/recipes')
    else:
        return render_template('new_recipe.html')


@app.route('/recipes/delete/<int:id>')
def delete(id):
    recipe = Recipe.query.get_or_404(id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect('/recipes')


@app.route('/recipes/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    recipe = Recipe.query.get_or_404(id)
    if request.method == 'POST':
        recipe.title = request.form['title']
        recipe.description = request.form['description']
        recipe.author = request.form['author']
        db.session.commit()
        return redirect('/recipes')
    else:
        return render_template('edit.html', recipe=recipe)


if __name__ == '__main__':
    app.run(debug=True)
