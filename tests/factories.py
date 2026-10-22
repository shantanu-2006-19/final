"""
Test Factory for Product Model
"""
import factory
from factory import fuzzy
from faker import Faker
from service.models import Product, Category

fake = Faker()


class ProductFactory(factory.Factory):
    """Generates fake Product instances for testing"""

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    description = factory.Faker("sentence", nb_words=6)
    price = fuzzy.FuzzyFloat(0.5, 999.99)
    available = factory.Faker("boolean")
    category = fuzzy.FuzzyChoice(
        choices=[
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ]
    )
