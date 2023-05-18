# from rest_framework.decorators import api_view
# from rest_framework import status
from rest_framework.response import Response
from product.serializers import ProductSerializers, CategorySerializers, ReviewSerializers, \
    ProductValidateSerializers, CategoryValidateSerializers, ReviewValidateSerializers
from product.models import Category, Product, Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def post(self, request, *args, **kwargs):
        serializer = ProductValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')
        product = Product.objects.create(title=title, description=description, price=price,
                                         category_id=category_id)
        return Response(data=ProductSerializers(product).data)


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = CategoryValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        category = Category.objects.create(name=name)
        return Response(data=CategorySerializers(category).data)


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def post(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        product_id = serializer.validated_data.get('product_id')
        review = Review.objects.create(text=text, stars=stars, product_id=product_id)
        return Response(data=ReviewSerializers(review).data)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------


# @api_view(['GET', 'POST'])
# def product_list_api_view(request):
#     print(request.user)
#     if request.method == 'GET':
#         ''' Get lists of objects '''
#         products = Product.objects.all()
#         ''' Serialize (Reformat) objects to dict '''
#         data_dict = ProductSerializers(instance=products, many=True).data
#         ''' Return data by JSON file '''
#         return Response(data=data_dict)
#     elif request.method == 'POST':
#         """ VALIDATE DATA """
#         serializer = ProductValidateSerializers(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         """ READ BODY """
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         price = serializer.validated_data.get('price')
#         product_id = serializer.validated_data.get('product_id')
#         """ CREATE PRODUCT """
#         product = Product.objects.create(title=title, description=description, price=price,
#                                          product_id=product_id)
#         product.save()
#         """ RETURN RESPONSE """
#         return Response(data=ProductSerializers(product).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail_api_view(request, id):
#     """ Check object """
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(data={'error': 'Product not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         """ Movie item serialize to dict """
#         data_dict = ProductSerializers(product, many=False).data
#         """ Return dict by JSON file """
#         return Response(data=data_dict)
#     elif request.method == 'PUT':
#         serializer = ProductValidateSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         product.title = request.data.get('title')
#         product.description = request.data.get('description')
#         product.price = request.data.get('price')
#         product.category_id = request.data.get('category_id')
#         product.save()
#         return Response(data=ProductSerializers(product).data,
#                         status=status.HTTP_202_ACCEPTED)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def category_list_api_view(request):
#     if request.method == 'GET':
#         category = Category.objects.all()
#         data_dict = CategorySerializers(category, many=True).data
#         return Response(data=data_dict)
#     elif request.method == 'POST':
#         serializer = CategoryValidateSerializers(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         name = serializer.validated_data.get('name')
#         category = Category.objects.create(name=name)
#         category.save()
#         return Response(data=CategorySerializers(category).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def category_detail_api_view(request, id):
#     try:
#         category = Category.objects.get(id=id)
#     except Category.DoesNotExist:
#         return Response(data={'error': 'Category not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data_dict = CategorySerializers(category, many=False).data
#         return Response(data=data_dict)
#     elif request.method == 'PUT':
#         serializer = CategoryValidateSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         category.name = request.data.get('name')
#         category.save()
#         return Response(data=CategorySerializers(category).data,
#                         status=status.HTTP_202_ACCEPTED)
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     if request.method == "GET":
#         reviews = Review.objects.all()
#         data_dict = ReviewSerializers(instance=reviews, many=True).data
#         return Response(data=data_dict)
#     elif request.method == "POST":
#         serializer = ReviewValidateSerializers(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#     text = serializer.validated_data.get('text')
#     product = serializer.validated_data.get('product')
#     stars = serializer.validated_data.get('stars')
#     review = Review.objects.create(text=text, product=product, stars=stars)
#     review.save()
#     return Response(data=ReviewSerializers(review).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'error': 'Review not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data_dict = ReviewSerializers(review, many=False).data
#         return Response(data=data_dict)
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review.text = request.data.get('text')
#         review.stars = request.data.get('stars')
#         review.product_id = request.data.get('product_id')
#         review.save()
#         return Response(data=ReviewSerializers(review).data,
#                         status=status.HTTP_202_ACCEPTED)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
