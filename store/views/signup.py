from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from store.models.productModel import Product
from store.models.categoryModel import Category
from store.models.customerModel import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('FirstName')
        last_name = postData.get('LastName')
        phone = postData.get('Contact')
        email = postData.get('email')
        password = postData.get('Password')

        # Server-side validation for Sign-up form.
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password
        )

        error_message = self.validateCustomer(customer)

        # Data storing in database.
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
        return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = 'Field Required: Please fill First Name to proceed'
        elif len(customer.first_name) < 4:
            error_message = 'Invalid Data: First Name must have at east 4 characters'
        elif not customer.last_name:
            error_message = 'Field Required: Please fill Last Name to proceed'
        elif len(customer.last_name) < 4:
            error_message = 'Invalid Data: Last Name must have at least 4 characters'
        elif not customer.phone:
            error_message = 'Field Required: Please fill Phone no. to proceed'
        elif len(customer.phone) < 4:
            error_message = 'Invalid Data: Phone no. must have at least 4 characters'
        elif not customer.password:
            error_message = 'Field Required: Please fill Password to proceed'
        elif len(customer.password) < 4:
            error_message = 'Invalid Data: Password must have at least 4 characters'
        elif customer.isExists():
            error_message = 'Email address already exist'

        return error_message
