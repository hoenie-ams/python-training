"""
The program that works with SQLAlchemy
"""

from models import Product
from db_session import session

# Add one
toothpaste = Product(name="Toothpaste", price=133)
milk = Product(name="Milk", price=215)
session.add(toothpaste)
session.add(milk)
session.commit()

# Add many
session.bulk_save_objects(
    [
        toothpaste, milk,
    ]
)
session.commit()


# Get all products
products = session.query(Product).all()
for p in products:
    print(p)

print(milk.id)
print(milk.price)
