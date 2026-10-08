from .models import Category, Product


class CategoryProductService:

    @staticmethod
    def view_category_product(category_name):
        category = Category.objects.filter(name=category_name)
        return Product.objects.filter(category=category)
