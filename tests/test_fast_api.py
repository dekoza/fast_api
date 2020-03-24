import json
import uuid

import orm
import pytest
from fastapi.testclient import TestClient

from demo.main import app
from demo.models import Cart, Item, db

client = TestClient(app)


def test_endpoint_bad_paload():
    bad_payload = {"bad": "payload"}
    response = client.post("/item", data=json.dumps(bad_payload))
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_endpoint_no_cookie():
    item_id = str(uuid.uuid4())

    async with db:
        with pytest.raises(orm.NoMatch):
            await Item.objects.get(external_id=item_id)

    # why does the dabase connection inside the app fail?

    payload = {"external_id": item_id, "name": "Test item", "value": 20}
    response = client.post("/item", json=payload)

    assert response.status_code == 204

    cart_id = response.cookies.get("cart_id")

    async with db:
        cart = await Cart.objects.get(id=cart_id)
        obj_num = Item.objects.filter(cart=cart, external_id=item_id).count()
        assert obj_num == 1


@pytest.mark.asyncio
async def test_endpoint_with_cookie():
    async with db:
        cart_id = str(uuid.uuid4())
        cart = await Cart.objects.create(id=cart_id)
        cart_item = await Item.objects.create(
            cart=cart, external_id=str(uuid.uuid4()), value=1, name="Initial"
        )

    payload = {"external_id": cart_item.external_id, "value": 100, "name": "Changed"}
    request, response = client.post("/item", json=payload, cookies={"cart_id": cart_id})
    assert response.status_code == 204

    async with db:
        cart = await Cart.objects.get(id=cart_id)
        assert cart.items.all().count()
