from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, Order, Profile, Support, Reviews
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    user = request.user
    products = Product.objects.all()
    return render(request,'index.html',{'products' : products, 'user' : user})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            print('****************Successfully logged in*****************')
            Profile.objects.create(username=username, name=username)
            print('*********Profile Created*******')
            return redirect('index')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            user = User.objects.create_user(username=username, password=password, email=username)
            user.save()
            login(request, user)
            print('****************Successfully registerd in*****************')
    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    print('*****************logout successful*****************')
    return redirect('index.html')

def cart(request):
    # CART ITEMS
    username = request.user.username
    Cart_items = Cart.objects.filter(username=username)

    # ORDERED ITEMS
    if Order.objects.filter(username=username).exists():
        order_items = Order.objects.filter(username=username)[0]
        return render(request, 'cart.html', {'cart_items':Cart_items, 'order_items':order_items})
    else:
        return render(request, 'cart.html')

def cart_buy(request, product_id):
    Cart_object = Cart.objects.get(id=product_id)
    Order.objects.create(username=Cart_object.username, product = Cart_object.product, quantity = Cart_object.quantity, price= Cart_object.price, image=Cart_object.image, status='Order Confirmed')
    print("**********************Order Placed***********************")
    Cart_object.delete()
    print("**************Deleted from Cart**************************")
    return render(request, 'cart.html')

@login_required(login_url='login')
def cart_order(request, product_id):
    if request.method == 'POST':
        name = request.user.username
        product = get_object_or_404(Product, id=product_id)
        image = product.image
        product_name = product.brand + product.model
        qty = int(request.POST.get('product_quantity'))
        total_price = product.price * qty
        if 'cart' in request.POST:
            Cart_check = Cart.objects.filter(username=name, product=product_name).exists()
            if Cart_check == True:
                print("*********************Already in the cart*******************")
            else:
                print("*********************Added in the cart*******************")
                Cart.objects.create(username=name, product = product_name, quantity = qty, price= total_price, image=image)

        elif 'buy' in request.POST:
            Order.objects.create(username=name, product = product_name, quantity = qty, price= total_price, image=image, status='Order Confirmed')
            print("*********************ORDER PLACED*******************")
    return render(request, 'cart.html')


def product(request, brand, model):
    products = get_object_or_404(Product, brand=brand, model=model)
    reviews = Reviews.objects.filter(product_id = products.id)[0:3]
    return render(request,'product.html',{'product' : products, 'reviews' : reviews})

@login_required(login_url='login')
def profile(request):
    username = request.user.username       
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        flat_building = request.POST.get('flat_building')
        landmark = request.POST.get('landmark')
        locality = request.POST.get('locality')
        city_state = request.POST.get('city_state')
        pin_code = request.POST.get('pin_code')
        Profile.objects.create(username=username, name=name, email=email, phone=phone, flat_no_building=flat_building,
            landmark=landmark,locality=locality, city_state=city_state, pin_code=pin_code)
        return render(request, 'profile.html')
    else:
        my_profile = Profile.objects.get(username=username)
        orders = Order.objects.filter(username=username) 
        return render(request,'profile.html',{'my_profile':my_profile ,'orders' : orders})

def support(request):
    if request.method == 'POST':
        username =request.user.username
        if 'password' in request.POST:
            type = 'p'
            query = 'Forgot Password'
            Support.objects.create(username=username, type=type, query=query)
            

        elif 'orders' in request.POST:
            type = 'd'
            query = 'Order Related'
            order_id = request.POST.get('order_id')
            Support.objects.create(username=username, type=type, order_id=order_id, query=query)

        elif 'other' in request.POST:
            type = 'o'
            query = request.POST.get('query')
            Support.objects.create(username=username, type=type, query=query)
    
    return render(request,'support.html')
