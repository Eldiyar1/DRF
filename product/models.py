from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    @property
    def product_count(self):
        return self.product.all().count()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')

    @property
    def rating(self):
        try:
            count = self.reviews.all().count()
            stars = sum([i.stars for i in self.reviews.all()])
            return stars // count
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return self.title

    @property
    def review_text(self):
        return [i.text for i in self.reviews.all()]


STARS = [
    (1, "1 star"),
    (2, "2 stars"),
    (3, "3 stars"),
    (4, "4 stars"),
    (5, "5 stars")
]


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')
    stars = models.PositiveIntegerField(choices=STARS, default=0)

    def __str__(self):
        return self.text
