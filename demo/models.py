import uuid

import databases
import orm
import sqlalchemy

from demo import config

db = databases.Database(config.DATABASE_URL)
meta = sqlalchemy.MetaData()


class Cart(orm.Model):
    __tablename__ = "cart"
    __database__ = db
    __metadata__ = meta

    id = orm.String(max_length=36, primary_key=True, default=lambda: str(uuid.uuid4()))


class Item(orm.Model):
    __tablename__ = "item"
    __database__ = db
    __metadata__ = meta

    id = orm.Integer(primary_key=True)
    external_id = orm.String(max_length=100, index=True)
    name = orm.String(max_length=100, allow_blank=True)
    value = orm.Integer(allow_null=True)
    cart = orm.ForeignKey(Cart)


engine = sqlalchemy.create_engine(str(db.url))
meta.create_all(engine)
