import json
from typing import List, Optional
from cart import dao
from products import Product, get_product


class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        """
        Represents a user's shopping cart.

        Args:
            id (int): Cart ID.
            username (str): Username associated with the cart.
            contents (List[Product]): List of products in the cart.
            cost (float): Total cost of the cart.
        """
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> "Cart":
        """
        Loads a Cart object from a dictionary.

        Args:
            data (dict): Dictionary containing cart data.

        Returns:
            Cart: An instance of the Cart class.
        """
        return Cart(
            id=data["id"],
            username=data["username"],
            contents=[Product(**item) for item in json.loads(data["contents"])],
            cost=data["cost"],
        )


def get_cart(username: str) -> List[Product]:
    """
    Retrieves the cart contents for a given username.

    Args:
        username (str): Username of the user.

    Returns:
        List[Product]: List of Product objects in the cart.
    """
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    products_list = []
    for cart_detail in cart_details:
        try:
            contents = json.loads(cart_detail["contents"])  # Safely parse the JSON string
        except json.JSONDecodeError:
            continue

        for product_id in contents:
            product = get_product(product_id)
            if product:
                products_list.append(product)

    return products_list


def add_to_cart(username: str, product_id: int) -> None:
    """
    Adds a product to the user's cart.

    Args:
        username (str): Username of the user.
        product_id (int): ID of the product to add.
    """
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int) -> None:
    """
    Removes a product from the user's cart.

    Args:
        username (str): Username of the user.
        product_id (int): ID of the product to remove.
    """
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str) -> None:
    """
    Deletes the user's cart.

    Args:
        username (str): Username of the user.
    """
    dao.delete_cart(username)
