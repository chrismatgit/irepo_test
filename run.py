from flask import Flask
from api.Views.routes import app


if __name__ == "__main__":
    app.run(debug=True)