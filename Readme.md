# Starting instructions

## Install Flask in the prepared python environment
> pip install flask
> pip install flask-sqlalchemy
> pip install Flask-Migrate

## Verify the flask version
> flask --version

## Create the requirement files:
> conda list -e >> requirements.txt
> conda env export > flask_env.yml

## To run the application
> flask run

## Starting the application
> python main.py

## Creating tables (Tables will be created in instance folder)
> python
>
> from main import db, app
>
> app_ctx = app.app_context()
>
> app_ctx.push()
>
> db.create_all()
>
> app_ctx.pop()
>
> exit()

## To handle migrations
1. Initialize
> flask --app main db init
2. Make the changes to the database
3. Generate the migration version and document it
> flask --app main db migrate -m "made description from recipes nullable" 
4. Apply changes to the database
> flask --app main db upgrade

## CRUD Operations
### C: creating & R: reading
> python
>
> from main import Recipe, db, app
>
> app_ctx = app.app_context()
>
> app_ctx.push()
>
> Recipe.query.all()
>
> db.session.add(Recipe(title="Pizza 1", description="Description for pizza 1", author="Joey"))
>
> pizza_2 = Recipe(title="Pizza 2", description="Description for pizza 2")
>
> db.session.add(pizza_2)
>
> Recipe.query.all()[0]
>
> Recipe.query.all()[1]
>
> Recipe.query.all()[5]  # IndexError
>
> Recipe.query.all()[0].title
>
> Recipe.query.all()[0].description
>
> Recipe.query.first()
>
> all_recipes = Recipe.query.all()
>
> all_recipes[0]
>
> Recipe.query.filter_by(title="Pizza 1").all()
>
> Recipe.query.get(1)  # Deprecated
>
> db.session.get(Recipe, 1)
>
> db.session.get(Recipe, 2) 
>
> db.session.get(Recipe, 5)  # Empty result
>
> db.session.commit()
>
> app_ctx.pop()
>
> exit()

### D: deleting
> python
>
> from main import Recipe, db, app
>
> app_ctx = app.app_context()
>
> app_ctx.push()
>
> Recipe.query.all()
>
> recipe_2 = db.session.get(Recipe, 2) 
>
> db.session.delete(recipe_2)
>
> Recipe.query.all()
>
> db.session.commit()
>
> app_ctx.pop()
>
> exit()


### U: updating
> python
>
> from main import Recipe, db, app
>
> app_ctx = app.app_context()
>
> app_ctx.push()
>
> Recipe.query.all()
>
> recipe_1 = db.session.get(Recipe, 1) 
>
> recipe_1.author
> 
> recipe_1.author = 'Monica' 
>
> db.session.commit()
>
> Recipe.query.filter_by(author="Monica").all()
>
> app_ctx.pop()
>
> exit()

## Other material
- [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/)
- [Visual Studio Code Set Up for Python Projects](https://codefinity.com/blog/Visual-Studio-Code-Set-Up-for-Python-Projects)
- [Build fast, responsive sites with Bootstrap](https://getbootstrap.com/)
- [Get started with Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/#quick-start)
- [Bootstrap Examples](https://getbootstrap.com/docs/5.3/examples/)
- [How do I format a date in Jinja2?](https://stackoverflow.com/questions/4830535/how-do-i-format-a-date-in-jinja2)
