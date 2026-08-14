from gimnasio_app.controllers import RoutineController
from gimnasio_app.views import RoutineView


def main() -> None:
    controller = RoutineController()
    view = RoutineView()
    print(view.render_week(controller.get_week()))
