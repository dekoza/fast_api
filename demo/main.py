from fastapi import FastAPI

from demo.views import item

app = FastAPI()
app.add_api_route("/item", item, methods=["POST"])
