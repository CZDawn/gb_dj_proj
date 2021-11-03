from django.test import TestCase

from mainapp.models import Product, ProductCategory


class ProductsTestCase(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(name='стулья')
        self.product_1 = Product.objects.create(
            name='стул 1',
            category=category,
            price=2000.00,
            quantity=10)
        self.product_2 = Product.objects.create(
            name='стул 2',
            category=category,
            price=1543.15,
            quantity=324)
        self.product_3 = Product.objects.create(
            name='стул 3',
            category=category,
            price=789.09,
            quantity=1222)

    def test_product_get(self):
        product_1 = Product.objects.get(name='стул 1')
        product_2 = Product.objects.get(name='стул 2')
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Product.objects.get(name='стул 1')
        product_2 = Product.objects.get(name='стул 2')
        self.assertEqual(str(product_1), 'стул 1 (стулья)')
        self.assertEqual(str(product_2), 'стул 2 (стулья)')

    def test_product_get_items(self):
        product_1 = Product.objects.get(name='стул 1')
        product_3 = Product.objects.get(name='стул 3')
        products = product_1.get_items()
        self.assertEqual(list(products), [product_1, product_3])

