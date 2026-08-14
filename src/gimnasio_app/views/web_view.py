from pathlib import Path

from flask import Flask, render_template

from gimnasio_app.controllers import RoutineController

_VIEWS_DIR = Path(__file__).parent


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=str(_VIEWS_DIR / "templates"),
        static_folder=str(_VIEWS_DIR / "static"),
    )
    controller = RoutineController()

    @app.route("/")
    def week():
        return render_template("week.html", routines=controller.get_week())

    return app


def run() -> None:
    create_app().run(debug=True)
