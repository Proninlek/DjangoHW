from django.shortcuts import render
from myapp.models import User, Product, Order


# Create your views here.

def index(request):
    users = []
    for i in User.objects.all():
        users.append(i)

    products = []
    for i in Product.objects.all():
        products.append(i)

    orders = []
    for i in Order.objects.all():
        orders.append(i)

    context = {
        'users': users,
        'products': products,
        'orders': orders
    }

    return render(request, 'myapp/index.html', context)