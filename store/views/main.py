from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.productModel import Product
from store.models.categoryModel import Category
from store.models.customerModel import Customer
from django.views import View


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()  # Get all categories.
    categoryID = request.GET.get('category')  # Get category-id from frontend.

    if categoryID:  # If categoryID is not emptystring, than get data from Product as per category-id.
        products = Product.get_all_products_by_id(categoryID)
    else:  # If categoryID is emptystring, than get all categories data from Product.
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    print('You are: ', request.session.get('customer_email'))
    return render(request, 'index.html', data)