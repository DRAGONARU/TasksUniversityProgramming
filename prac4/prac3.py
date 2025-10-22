class Product:
    """
    Класс, представляющий товар в магазине.

    Атрибуты:
        name (str): Название товара.
        price (float): Цена товара.
        category (str): Категория, к которой принадлежит товар.
        stock (int): Количество единиц товара на складе.
    """
    def __init__(self, name, price, category, stock):
        """
        Инициализация объекта Product.

        Args:
            name (str): Название товара.
            price (float): Цена товара.
            category (str): Категория товара.
            stock (int): Количество товара на складе.
        """
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def is_available(self, quantity):
        """
        Проверяет, доступно ли указанное количество товара на складе.

        Args:
            quantity (int): Запрашиваемое количество.

        Returns:
            bool: True, если товара достаточно, иначе False.
        """
        return self.stock >= quantity

    def reduce_stock(self, quantity):
        """
        Уменьшает количество товара на складе, если его достаточно.

        Args:
            quantity (int): Количество товара для списания.
        """
        if self.is_available(quantity):
            self.stock -= quantity


class Customer:
    """
    Класс, описывающий покупателя.

    Атрибуты:
        name (str): Имя покупателя.
        email (str): Электронная почта покупателя.
        order_history (list): Список оформленных заказов.
    """
    def __init__(self, name, email):
        """
        Инициализация объекта Customer.

        Args:
            name (str): Имя покупателя.
            email (str): Электронная почта покупателя.
        """
        self.name = name
        self.email = email
        self.order_history = []

    def add_order_to_history(self, order):
        """
        Добавляет заказ в историю покупателя.

        Args:
            order (Order): Объект заказа.
        """
        self.order_history.append(order)

    def __str__(self):
        """
        Возвращает строковое представление покупателя.

        Returns:
            str: Строка с именем и почтой покупателя.
        """
        return f"Покупатель: {self.name} ({self.email})"


class ShoppingCart:
    """
    Класс, представляющий корзину покупателя.

    Атрибуты:
        items (dict): Словарь с товарами и их количеством (ключ — Product, значение — int).
    """
    def __init__(self):
        """Создает пустую корзину."""
        self.items = {}

    def add_product(self, product, quantity=1):
        """
        Добавляет товар в корзину.

        Args:
            product (Product): Товар для добавления.
            quantity (int): Количество добавляемого товара (по умолчанию 1).
        """
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product):
        """
        Удаляет товар из корзины.

        Args:
            product (Product): Товар для удаления.
        """
        if product in self.items:
            del self.items[product]

    def update_quantity(self, product, quantity):
        """
        Обновляет количество товара в корзине.
        Если количество ≤ 0, товар удаляется.

        Args:
            product (Product): Товар для обновления.
            quantity (int): Новое количество.
        """
        if quantity <= 0:
            self.remove_product(product)
        elif product.is_available(quantity):
            self.items[product] = quantity

    def calculate_total(self):
        """
        Вычисляет общую стоимость всех товаров в корзине.

        Returns:
            float: Общая сумма.
        """
        return sum(p.price * q for p, q in self.items.items())

    def clear_cart(self):
        """Очищает корзину."""
        self.items.clear()


class Order:
    """
    Класс, представляющий заказ.

    Атрибуты:
        customer (Customer): Покупатель, оформивший заказ.
        cart (ShoppingCart): Корзина с товарами.
        total (float): Итоговая сумма заказа с учетом скидки и налога.

    Константы:
        TAX_RATE (float): Налоговая ставка (10%).
        DISCOUNT_RATE (float): Скидка при больших суммах (5%).
    """
    TAX_RATE = 0.1
    DISCOUNT_RATE = 0.05

    def __init__(self, customer, cart):
        """
        Инициализация заказа.

        Args:
            customer (Customer): Покупатель.
            cart (ShoppingCart): Корзина с товарами.
        """
        self.customer = customer
        self.cart = cart
        self.total = 0

    def calculate_total(self):
        """
        Рассчитывает итоговую сумму заказа:
        применяет скидку при сумме > 5000 и добавляет налог.

        Returns:
            float: Общая сумма с учетом скидки и налога.
        """
        subtotal = self.cart.calculate_total()
        discount = subtotal * self.DISCOUNT_RATE if subtotal > 5000 else 0
        tax = (subtotal - discount) * self.TAX_RATE
        self.total = subtotal - discount + tax
        return self.total

    def finalize_order(self):
        """
        Завершает оформление заказа:
        - уменьшает количество товаров на складе;
        - добавляет заказ в историю покупателя;
        - очищает корзину.
        """
        for product, quantity in self.cart.items.items():
            product.reduce_stock(quantity)
        self.customer.add_order_to_history(self)
        self.cart.clear_cart()
