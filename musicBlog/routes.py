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

@app.route('/login')
def login():
    return "Login";


