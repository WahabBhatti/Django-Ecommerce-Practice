from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.productModel import Product
from store.models.categoryModel import Category
from store.models.customerModel import Customer
from django.views import View



class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('Password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                return redirect('homepage')
            else:
                error_message = 'Invalid Email or Password!!'
        else:
            error_message = 'Invalid Email or Password!!'

        return render(request, 'login.html', {'error': error_message})
