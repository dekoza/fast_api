import uuid

from fastapi import APIRouter, Cookie, Response, status
from orm import NoMatch

from demo.models import Cart as CartModel
from demo.models import Item as ItemModel
from demo.serializers import Item

router = APIRouter()


@router.post("/item")
async def item(item: Item, response: Response, cart_id: str = Cookie(None)):
    if not cart_id:
        cart_id = str(uuid.uuid4())
        response.set_cookie(key="cart_id", value=cart_id)
    try:
        cart = await CartModel.objects.get(id=cart_id)
    except NoMatch:
        cart = await CartModel.objects.create(id=cart_id)

    try:
        cart_item = await ItemModel.objects.get(
            external_id=item.external_id, cart=cart,
        )
        await cart_item.update(**item.dict())
    except NoMatch:
        await ItemModel.objects.create(**item.dict())
    response.status_code = status.HTTP_204_NO_CONTENT
    return response
