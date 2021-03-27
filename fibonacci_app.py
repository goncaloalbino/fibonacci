import connexion
from connexion.resolver import RestyResolver

if __name__ == "__main__":
    app = connexion.FlaskApp(__name__, specification_dir="openapi/")
    app.add_api("fibonacci_api.yaml", resolver=RestyResolver("api"))
    app.run(port=8000)
