from app import create_app
from app.cli import manage


app = create_app()
manage.register(app)


if __name__ == "__main__":
    app.run()
