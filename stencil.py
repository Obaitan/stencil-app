from app import app, db
from app.models import Character, Resource, User, Circle, Record

if __name__ == "__main__":
    app.run(debug=True)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 'User': User, 'Circle': Circle, 'Resource': Resource, 'Record': Record, 'Character': Character
    }