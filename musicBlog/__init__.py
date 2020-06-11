from flask import Flask

app = Flask(__name__)

# ? Important to be kept at the end.
from musicBlog import routes
