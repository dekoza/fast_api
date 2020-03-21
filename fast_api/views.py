import uuid

from pony.orm import db_session, commit
from sanic.response import json, empty

from fast_api.models import Cart, Item

accepted_params = ["external_id", "name", "value"]


async def item(request):
    if not request.json:
        return json({"error": "missing payload"}, status=400)

    cart_id = request.cookies.get("cart_id", str(uuid.uuid4()))
    data = {key: value for key, value in request.json.items() if key in accepted_params}

    external_id = data.get("external_id")
    if not external_id:
        return json({"error": "missing 'external_id'"}, status=400)

    with db_session():
        cart = Cart.get(id=cart_id) or Cart(id=cart_id)

        cart_item = Item.get(external_id=external_id, cart=cart) or Item(
            external_id=external_id, cart=cart
        )
        cart_item.set(cart=cart, **data)

    response = empty()
    response.cookies["cart_id"] = cart_id
    return response
