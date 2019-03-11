from app.load import create_app
from decouple import config

app = create_app()

if __name__ == '__main__':
    app.run(debug=config("DEBUG"))