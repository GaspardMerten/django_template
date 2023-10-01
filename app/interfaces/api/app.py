from ninja import NinjaAPI

from .views import hello_world

__all__ = ["app"]

app = NinjaAPI()

app.add_router("", hello_world.router)
