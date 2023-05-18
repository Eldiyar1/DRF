from rest_framework import serializers
from product.models import Category, Product, Review
from rest_framework.exceptions import ValidationError


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name product_count'.split()


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description price rating review_text'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text product stars'.split()


class ProductValidateSerializers(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=1, max_length=10)
    description = serializers.CharField(required=False)
    price = serializers.FloatField(min_value=1)
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):  # 100
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            class Meta:
                raise ValidationError("Category does not exist")
            return category_id


class CategoryValidateSerializers(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=1, max_length=10)


class ReviewValidateSerializers(serializers.Serializer):
    text = serializers.CharField(required=True)
    stars = serializers.IntegerField(min_value=1)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):  # 100
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            class Meta:
                raise ValidationError("Product does not exist")

            return product_id
