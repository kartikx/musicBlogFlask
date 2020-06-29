from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from is_safe_url import is_safe_url
from musicBlog import app, bcrypt, db, login_manager
from musicBlog.forms import LoginForm, RegistrationForm
from musicBlog.models import User, Post

posts = [
    {'username': "kartikx",
    'title': "First Post",
    'content': "Welcome to my first page!",
    'date_posted': "11/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
    {'username': "kartikx",
    'title': "Second Post",
    'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quaerat porro laudantium officiis accusamus, rem illo laborum ratione unde reiciendis, dolores, harum officia maxime atque vel voluptatibus nesciunt tempora! Dolore, nihil.",
    'date_posted': "12/06/2020"
    },
]

@app.route('/')
def welcome():
    # ? Add check to see if logged in.
    return render_template("welcome.html", title="Home")

@app.route('/feed')
def feed():
    return render_template("feed.html", title="Feed", posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created, you may now log in", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title="Sign Up", form=form)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    '''
    I have added checking for Username existence
    in the Login Form itself. So I can be sure that
    if the form validated, the User exists.
    I do need to check whether passwords match, however.
    '''
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            '''
            It might be possible, that the user was trying to go
            to a Login Restricted page, hence we'll redirect him
            to the page he was trying to go to.
            '''
            next_url = request.args.get('next')
            # ? This prevents security exploits.
            if not is_safe_url(next_url, {"localhost:5000"}):
                return abort(400)
            flash("Welcome back!", "success")
            redirect_to_page = next_url or url_for('feed') 
            return redirect(redirect_to_page)
        else:
            flash("Please check your username and password.", "danger")
    return render_template("login.html", title="Login", form=form);

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('welcome'))

