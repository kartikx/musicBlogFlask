from flask import render_template
from musicBlog import app

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
    return "Login";


