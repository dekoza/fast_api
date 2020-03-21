from sanic import Sanic

from fast_api.views import item

app = Sanic(name="fast_api")
app.add_route(item, "/item", methods=["POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
