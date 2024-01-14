from pytest_factoryboy import register

from . import factories

register(factory_class=factories.PostFactory)
