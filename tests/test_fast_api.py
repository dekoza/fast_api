import json
import uuid

from pony.orm import db_session, count, select

from fast_api.main import app
from fast_api.models import Cart, Item


def test_endpoint_bad_paload():
    bad_payload = {"bad": "payload"}
    request, response = app.test_client.post("/item", data=json.dumps(bad_payload))
    assert response.status_code == 400


def test_endpoint_no_cookie():
    item_id = str(uuid.uuid4())

    with db_session():
        query = select(i for i in Item if i.external_id == item_id)
        assert len(query) == 0

    payload = {"external_id": item_id, "name": "Test item", "value": 20}
    request, response = app.test_client.post("/item", data=json.dumps(payload))
    assert response.status_code == 204
    cart_id = response.cookies.get("cart_id")

    with db_session():
        cart = Cart.get(id=cart_id)
        assert cart is not None

        query = select(i for i in Item if i.external_id == item_id and i.cart == cart)
        assert len(query) == 1


def test_endpoint_with_cookie():
    with db_session():
        cart_id = str(uuid.uuid4())
        cart = Cart(id=cart_id)
        cart_item = Item(cart=cart, external_id=str(uuid.uuid4()), value=1, name="Initial")

    payload = {"external_id": cart_item.external_id, "value": 100, "name": "Changed"}
    request, response = app.test_client.post("/item", data=json.dumps(payload), cookies={"cart_id": cart_id})

    assert response.status_code == 204

    with db_session():
        cart = Cart.get(id=cart_id)
        assert len(cart.items) == 1
        db_item = cart.items.copy().pop()
        assert db_item.external_id == cart_item.external_id



