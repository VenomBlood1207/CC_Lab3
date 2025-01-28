from products import dao

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> 'Product':
        """Load a Product instance from a dictionary."""
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    """Retrieve a list of all products."""
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """Retrieve a single product by its ID."""
    return Product.load(dao.get_product(product_id))


def add_product(product: dict) -> None:
    """Add a new product using a dictionary."""
    dao.add_product(product)


def update_qty(product_id: int, qty: int) -> None:
    """Update the quantity of a product."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
