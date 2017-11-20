from app import create_app, db
from flask_cors import CORS
from flask_migrate import Migrate

application = create_app()
CORS(application)

migrate = Migrate(application, db)


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8081)
