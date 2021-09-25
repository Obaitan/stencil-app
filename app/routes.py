from app import app


@app.route("/")
@app.route("/login")
def login():
    return "<h1>This is the login page</h1>"