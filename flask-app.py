from app import create_app, db
from flask_migrate import Migrate

application = create_app()

migrate = Migrate(application, db)


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8081)
