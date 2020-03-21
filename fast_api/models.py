import uuid

from pony import orm

from fast_api import config

db = orm.Database(**config.DATABASE)


class Cart(db.Entity):
    id = orm.PrimaryKey(uuid.UUID, default=uuid.uuid4)
    items = orm.Set("Item")


class Item(db.Entity):
    external_id = orm.Required(str, index=True)
    name = orm.Optional(str)
    value = orm.Optional(int)
    cart = orm.Required(Cart)


db.generate_mapping(create_tables=True)
