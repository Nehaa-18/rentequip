from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import CustomUser  # Assuming you have a CustomUser model
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import CustomUser

# Create your views here.
@never_cache  # Add this decorator to prevent caching
def index(request):
    return render(request,'index.html')
#@never_cache
#def logout_view(request):
    #if request.user.is_authenticated:
        #logout(request)
    #return redirect('index')
@never_cache
def about(request):
    return render(request,'about.html')

@never_cache
def contact(request):
    return render(request,'contact.html')

@never_cache
def user_profile(request):
    return render(request,'user_profile.html',{'user': request.user})

@never_cache
def account(request):
    return render(request,'account.html')

@never_cache
def order(request):
    return render(request,'order.html')

@never_cache
def rent(request):
    return render(request,'rent.html')

@never_cache
def movingequip(request):
    return render(request,'movingequip.html')

@never_cache
def addequip(request):
    return render(request,'addequip.html')

@never_cache
@login_required(login_url='login')
def admindash(request):
     if request.user.is_superuser:
        users = CustomUser.objects.exclude(is_superuser=True)
        return render(request, "admindash.html", {"users": users})
        return redirect("home")
     
@login_required(login_url='login')
def dashboardOrg(request):
     if request.user.is_superuser:
        users = CustomUser.objects.exclude(is_superuser=True)
        return render(request, "dashboardOrg.html", {"users": users})
     return render(request, "dashboardOrg.html", {})
     
@never_cache
def dashboard(request):
    return render(request,'dashboard.html')

@never_cache
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']  # Make sure this matches your form field name
        usertype = request.POST['usertype']

        if password != confirm_password:
            # Handle password mismatch error
            return render(request, 'registration.html', {'error_message': 'Passwords do not match'})

        # Create a new user object
        user = CustomUser.objects.create_user(username=username, email=email, password=password, usertype=usertype)
        # You may want to do additional processing here if needed
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')  # Redirect to login page after successful registration
        
    return render(request,'registration.html')



from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
@never_cache
def login(request):
    if request.method == 'POST':
        loginusername = request.POST.get('username')
        password = request.POST.get('password')

        if loginusername and password:  # Use 'loginusername' here
            # Check if the entered credentials are for the admin
            if loginusername == "admin" and password == "Ajce24@mca":
                users = CustomUser.objects.exclude(is_superuser='1')  # Exclude superusers
                user_count = users.count()
                context = {
                    "users": users,
                    "user_count": user_count
                }
                return render(request, 'admindash.html', context)
            else:
                # For regular users, attempt to authenticate
                user = authenticate(request, username=loginusername, password=password)

                if user is not None:
                    auth_login(request, user)
                    request.session['username'] = user.username
                    if user.usertype == 'User':
                        return redirect('dashboard')
                    elif user.usertype == 'Company':
                        return redirect('dashboardOrg')
                    else:
                        return redirect('admindash')
                else:
                    error_message = "Invalid username or email"
                    return render(request, 'login.html', {'error_message': error_message})
        else:
            error_message = "email and password are required"
            return render(request, 'login.html', {'error_message': error_message})
    response = render(request, 'login.html')
    response['Cache-Control'] = 'no-store,must-revalidate'
    return response

    
@never_cache
def handlelogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

@never_cache
def logout(request):
    auth.logout(request)
    return redirect("/")


from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
#from .models import MyUser
from django.template.loader import render_to_string
@never_cache
def deactivate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if user.is_active:
        user.is_active = False
        user.save()
         # Send deactivation email
        subject = 'Account Deactivation'
        message = 'Your account has been deactivated by the admin.'
        from_email = 'nehaa2024b@mca.ajce.in'  # Replace with your email
        recipient_list = [user.email]
        html_message = render_to_string('deactivation_mail.html', {'user': user})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)

        messages.success(request, f"User '{user.username}' has been deactivated, and an email has been sent.")
    else:
        messages.warning(request, f"User '{user.username}' is already deactivated.")
    return redirect('admindash')
@never_cache
def activate_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not user.is_active:
        user.is_active = True
        user.save()
        subject = 'Account activated'
        message = 'Your account has been activated.'
        from_email = 'nehaa2024b@mca.ajce.in'  # Replace with your email
        recipient_list = [user.email]
        html_message = render_to_string('activation_mail.html', {'user': user})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    else:
        messages.warning(request, f"User '{user.username}' is already active.")
    return redirect('admindash')




from django.shortcuts import render, redirect
from decimal import Decimal, InvalidOperation
from .models import Product
from django.http import HttpResponseRedirect
def addequip(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        price_per_day = request.POST.get('price_per_day')
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        availability = request.POST.get('availability')
        image = request.FILES.get('image')

        try:
            if rating is not None:
                rating = Decimal(rating)
            if price_per_day is not None:
                price_per_day = Decimal(price_per_day)
        except (InvalidOperation, TypeError, ValueError):
            return render(request, 'error.html', {'message': 'Invalid input for rating or price.'})

        if name and description and category and image:
            product = Product(
                name=name,
                description=description,
                rating=rating if rating is not None else Decimal('0'),
                price_per_day=price_per_day if price_per_day is not None else Decimal('0'),
                category=category,
                subcategory=subcategory,
                availability=availability,
                image=image,
                
            )
            product.save()
            return HttpResponseRedirect('view_equip')
    
    # Add a return statement for the case where the conditions aren't met
    return render(request, 'addequip.html')




def view_equip(request):
    # Query the database to get all bus objects
    equips = Product.objects.all()

    # Create a context dictionary to pass the bus data to the template
    context = {
        'equips': equips
    }

    # Render the template and pass the context
    return render(request, 'view_equip.html',context)


@never_cache
def product(request):
   products = Product.objects.all()  # Retrieve all products
   return render(request, 'product.html', {'products': products})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


from .models import Product, Cart, CartItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart')


def remove_from_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = Cart.objects.get(user=request.user)
    try:
        cart_item = cart.cartitem_set.get(product=product)
        if cart_item.quantity >= 1:
             cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    
    return redirect('cart')

# def view_cart(request):
    
#     if request.user.is_authenticated:
#         cart = request.user.cart
#         cart_items = CartItem.objects.filter(cart=cart)
#     return render(request, 'cart.html', {'cart_items': cart_items})

def view_cart(request):
    cart_items = None  # Initialize cart_items

    if request.user.is_authenticated:
        cart = request.user.cart
        cart_items = CartItem.objects.filter(cart=cart)

    return render(request, 'cart.html', {'cart_items': cart_items})



def increase_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')


def decrease_cart_item(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart = request.user.cart
    cart_item = cart.cartitem_set.get(product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

def fetch_cart_count(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart = request.user.cart
        cart_count = CartItem.objects.filter(cart=cart).count()
    return JsonResponse({'cart_count': cart_count})

def get_cart_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart=request.user.cart)
        cart_count = cart_items.count()
    else:
        cart_count = 0
    return cart_count




from django.shortcuts import render
from .models import CustomUser

def usertypecount(request):
    user_count = CustomUser.objects.filter(usertype='User').count()
    company_count = CustomUser.objects.filter(usertype='Company').count()
    
    context = {
        'user_count': user_count,
        'company_count': company_count,
    }
    
    return render(request, 'usertypecount.html', context)




from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # Extract updated data from the request
        name = request.POST.get('name')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        price_per_day = request.POST.get('price_per_day')
        category = request.POST.get('category')
        availability = request.POST.get('availability')
        image = request.FILES.get('image')

        try:
            if rating is not None:
                rating = Decimal(rating)
            if price_per_day is not None:
                price_per_day = Decimal(price_per_day)
        except (InvalidOperation, TypeError, ValueError):
            return render(request, 'error.html', {'message': 'Invalid input for rating or price.'})

        # Update the product model with the new data
        product.name = name
        product.description = description
        product.rating = rating if rating is not None else Decimal('0')
        product.price_per_day = price_per_day if price_per_day is not None else Decimal('0')
        product.category = category
        product.availability = availability
        if image:
            product.image = image

        # Save the updated product
        product.save()
        return redirect('admindash')
    
    return render(request, 'edit_product.html', {'product': product})




from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('admindash')

    return render(request, 'delete_product.html', {'product': product})





# @login_required
# def account(request):
#     if request.method == 'POST':
#         # Get the current user
#         user = request.user

#         # Update user's profile data with the new values from the form
#         user.first_name = request.POST['first-name']
#         user.last_name = request.POST['last-name']
#         user.username = request.POST['username']
#         user.email = request.POST['email']

#         # Additional fields like phone number and address can be saved in a separate user profile model
#         user_profile = user.userprofile
#         user_profile.phone_number = request.POST['phone-number']
#         user_profile.address = request.POST['address']

#         user.save()
#         user_profile.save()

#         return redirect('account')  # Redirect to the profile view after saving changes

#     # If it's a GET request, pre-fill the form fields with the current user's data
#     user = request.user
#     user_profile = user.userprofile
#     context = {
#         'user': user,
#         'user_profile': user_profile
#     }
#     return render(request, 'account.html', context)




@never_cache
def regusers(request):
    users = CustomUser.objects.filter(usertype='User', is_superuser=False)    
    user_count = users.count()
    context = {
        "users": users,
        "user_count": user_count
    }
    return render(request,'regusers.html',context)


@never_cache
def cusers(request):
    users = CustomUser.objects.filter(usertype='Company', is_superuser=False)    
    user_count = users.count()
    context = {
        "users": users,
        "user_count": user_count
    }
    return render(request,'cusers.html',context)







from django.shortcuts import render, redirect
from .models import CompanyProfile
from .models import UserProfile

@never_cache
@login_required
def account(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user if request.user.is_authenticated else None)
    
    if request.method == 'POST':
        # Update the user's fields
        user_instance = request.user
        user_instance.first_name = request.POST.get('first_name')
        user_instance.last_name = request.POST.get('last_name')
        user_instance.email = request.POST.get('email')
        user_instance.username = request.POST.get('username')
        user_instance.save()

        # Update the user profile fields
        user_profile.address = request.POST.get('address')
        user_profile.phone_number = request.POST.get('phone_number')
        user_profile.pincode = request.POST.get('pincode')
        user_profile.save()

        messages.success(request, 'Profile updated successfully')
       

    context = {
        'user_profile': user_profile
    }
    return render(request, 'account.html', context)




from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import CompanyProfile

@login_required
@never_cache
def accountorg(request):
    # Get or create the CompanyProfile for the authenticated user
    company_profile, created = CompanyProfile.objects.get_or_create(user=request.user if request.user.is_authenticated else None)

    if request.method == 'POST':
        # Update the company profile fields based on the form data
        company_profile.company_name = request.POST.get('company_name')
        company_profile.phone_number = request.POST.get('phone_number')
        company_profile.website = request.POST.get('website')
        company_profile.pincode = request.POST.get('pincode')
        company_profile.address = request.POST.get('address')
       # Save the updated company profile
        company_profile.save()

        # Update User related fields
        user_instance = request.user  # Assuming CustomUser is used
        user_instance.first_name = request.POST.get('first_name')
        user_instance.last_name = request.POST.get('last_name')
        user_instance.email = request.POST.get('email')
        user_instance.username = request.POST.get('username')
        user_instance.save()
        

        messages.success(request, 'Profile updated successfully')

    context = {
        'company_profile': company_profile
    }
    return render(request, 'accountorg.html', context)




from django.shortcuts import render
from .models import Product
@login_required
@never_cache
def movingequip(request):
    movingequip = Product.objects.filter(category='moving')
    context = {
        'products': movingequip
    }
    return render(request, 'movingequip.html', context)


@login_required
@never_cache
def dumpsterequip(request):
    dumpsterequip = Product.objects.filter(category='dumpster')
    context = {
        'products': dumpsterequip
    }
    return render(request, 'dumpsterequip.html', context)

@login_required
@never_cache
def sportsequip(request):
    sportsequip = Product.objects.filter(category='sports')
    context = {
        'products': sportsequip
    }
    return render(request, 'sportsequip.html', context)

@login_required
@never_cache
def officeequip(request):
    officeequip = Product.objects.filter(category='office')
    context = {
        'products': officeequip
    }
    return render(request, 'officeequip.html', context)

@login_required
@never_cache
def visualequip(request):
    visualequip = Product.objects.filter(category='visual')
    context = {
        'products': visualequip
    }
    return render(request, 'visualequip.html', context)

@login_required
@never_cache
def audioequip(request):
    audioequip = Product.objects.filter(category='audio')
    context = {
        'products': audioequip
    }
    return render(request, 'audioequip.html', context)



from django.shortcuts import render, get_object_or_404
from .models import Product
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})



from django.http import JsonResponse
from .models import Product  # Replace with your Product model import
def search_products(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    # Perform a search query using your Product model based on the received query
    products = Product.objects.filter(name__icontains=query)[:5]  # Adjust as needed

    # Create a list of products' names to send back as JSON response
    products_list = [{'name': product.name} for product in products]

    return JsonResponse({'products': products_list})



# from django.shortcuts import get_object_or_404, HttpResponse
# from .models import Wishlist, Product
# def toggle_wishlist(request):
#     if request.method == 'GET' and request.is_ajax():
#         product_id = request.GET.get('product_id')
#         user = request.user  # Assuming the user is authenticated

#         try:
#             wishlist_item = Wishlist.objects.get(user=user, product_id=product_id)
#             wishlist_item.delete()
#             status = 'removed'
#         except Wishlist.DoesNotExist:
#             Wishlist.objects.create(user=user, product_id=product_id)
#             status = 'added'

#         return JsonResponse({'status': status})
#     return JsonResponse({'status': 'error'})

# from django.shortcuts import render
# from .models import Wishlist

# def wishlist_view(request):
#     # Get the wishlist items for the current user
#     wishlist_items = Wishlist.objects.filter(user=request.user)

#     context = {
#         'wishlist_items': wishlist_items
#     }

#     return render(request, 'wishlist.html', context)



# from .models import CustomUser,Product, Cart, CartItem, Order, OrderItem
# from django.http import JsonResponse
# from django.conf import settings
# import razorpay
# import json
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def create_order(request):
#     if request.method == 'POST':
#         user = request.user
#         cart = user.cart

#         cart_items = CartItem.objects.filter(cart=cart)
#         total_amount = sum(item.product.price * item.quantity for item in cart_items)

#         try:
#             order = Order.objects.create(user=user, total_amount=total_amount)
#             for cart_item in cart_items:
#                 OrderItem.objects.create(
#                     order=order,
#                     product=cart_item.product,
#                     quantity=cart_item.quantity,
#                     item_total=cart_item.product.price * cart_item.quantity
#                 )

#             client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
#             payment_data = {
#                 'amount': int(total_amount * 100),
#                 'currency': 'INR',
#                 'receipt': f'order_{order.id}',
#                 'payment_capture': '1'
#             }
#             orderData = client.order.create(data=payment_data)
#             order.payment_id = orderData['id']
#             order.save()

#             return JsonResponse({'order_id': orderData['id']})
        
#         except Exception as e:
#             print(str(e))
#             return JsonResponse({'error': 'An error occurred. Please try again.'}, status=500)
        


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# import razorpay
# import json
# from .models import CartItem, Order, OrderItem
# from django.conf import settings
from .models import  Product, Cart, CartItem, Order, OrderItem
from django.http import JsonResponse
from django.conf import settings
import razorpay
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            user = request.user
            cart = user.cart

            cart_items = CartItem.objects.filter(cart=cart)
            total_amount = sum(item.product.price_per_day * item.quantity for item in cart_items)

            order = Order.objects.create(user=user, total_amount=total_amount)
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    item_total=cart_item.product.price_per_day * cart_item.quantity
                )

            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            payment_data = {
                'amount': int(total_amount * 100),
                'currency': 'INR',
                'receipt': f'order_{order.id}',
                'payment_capture': '1'
            }
            order_data = client.order.create(data=payment_data)
            order.payment_id = order_data['id']
            order.save()

            return JsonResponse({'order_id': order_data['id']})

        except Exception as e:
            print(str(e))
            return JsonResponse({'error': 'An error occurred. Please try again.'}, status=500)





@login_required
@never_cache
def checkout(request):
    cart_items = CartItem.objects.filter(cart=request.user.cart)
    total_amount = sum(item.product.price_per_day * item.quantity for item in cart_items)

    cart_count = get_cart_count(request)
    email = request.user.email
    first_name = request.user.first_name

    context = {
        'cart_count': cart_count,
        'cart_items': cart_items,
        'total_amount': total_amount,
        'email':email,
        'first_name':first_name
    }
    return render(request, 'checkout.html', context)


@csrf_exempt
def handle_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        razorpay_order_id = data.get('order_id')
        payment_id = data.get('payment_id')

        try:
            order = Order.objects.get(payment_id=razorpay_order_id)

            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            payment = client.payment.fetch(payment_id)

            if payment['status'] == 'captured':
                order.payment_status = True
                order.save()
                user = request.user
                user.cart.cartitem_set.all().delete()
                return JsonResponse({'message': 'Payment successful'})
            else:
                return JsonResponse({'message': 'Payment failed'})

        except Order.DoesNotExist:
            return JsonResponse({'message': 'Invalid Order ID'})
        except Exception as e:

            print(str(e))
            return JsonResponse({'message': 'Server error, please try again later.'})
        

from django.shortcuts import render, get_object_or_404
from .models import Order

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_detail.html', {'order': order})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})



from django.shortcuts import render, redirect
from .models import Wishlist
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, f"{product.name} added to your wishlist!")
    else:
        messages.info(request, f"{product.name} is already in your wishlist!")
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        wishlist_item = Wishlist.objects.get(user=request.user, product=product)
        wishlist_item.delete()
        messages.success(request, f"{product.name} removed from your wishlist!")
    except Wishlist.DoesNotExist:
        messages.error(request, f"{product.name} was not in your wishlist!")
    return redirect('wishlist')

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    context = {'wishlist_items': wishlist_items}
    return render(request, 'wishlist.html', context)


from django.shortcuts import render
from .models import Product

def search_blog(request):
    query = request.GET.get('q')

    if query:
        results = Product.objects.filter(name__icontains=query)
    else:
        results = None

    return render(request, 'search_results.html', {'results': results, 'query': query})

from django.shortcuts import render
from .models import Product

def search_results(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = Product.objects.filter(name__icontains=query)

    return render(request, 'search_results.html', {'results': results, 'query': query})



from django.shortcuts import render
from .models import Product  # Import your Product model or relevant model

def search_mov(request):
    query = request.GET.get('q')
    results = Product.objects.filter(category='moving', name__icontains=query) if query else Product.objects.none()
    
    context = {
        'results': results,
    }
    return render(request, 'search_mresults.html', context)

def search_mresults(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = Product.objects.filter(name__icontains=query)

    return render(request, 'search_mresults.html', {'results': results, 'query': query})


def search_audio(request):
    query = request.GET.get('q')
    results = Product.objects.filter(category='audio', name__icontains=query) if query else Product.objects.none()
    
    context = {
        'results': results,
    }
    return render(request, 'search_aresults.html', context)

def search_aresults(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = Product.objects.filter(name__icontains=query)

    return render(request, 'search_aresults.html', {'results': results, 'query': query})

def search_office(request):
    query = request.GET.get('q')
    results = Product.objects.filter(category='office', name__icontains=query) if query else Product.objects.none()
    
    context = {
        'results': results,
    }
    return render(request, 'search_oresults.html', context)

def search_oresults(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = Product.objects.filter(name__icontains=query)

    return render(request, 'search_oresults.html', {'results': results, 'query': query})

def search_visual(request):
    query = request.GET.get('q')
    results = Product.objects.filter(category='visual', name__icontains=query) if query else Product.objects.none()
    
    context = {
        'results': results,
    }
    return render(request, 'search_vresults.html', context)

def search_vresults(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = Product.objects.filter(name__icontains=query)

    return render(request, 'search_vresults.html', {'results': results, 'query': query})

def search_dum(request):
    query = request.GET.get('q')
    results = Product.objects.filter(category='dumpster', name__icontains=query) if query else Product.objects.none()
    
    context = {
        'results': results,
    }
    return render(request, 'search_dresults.html', context)

def search_dresults(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = Product.objects.filter(name__icontains=query)

    return render(request, 'search_dresults.html', {'results': results, 'query': query})

def search_sports(request):
    query = request.GET.get('q')
    results = Product.objects.filter(category='sports', name__icontains=query) if query else Product.objects.none()
    
    context = {
        'results': results,
    }
    return render(request, 'search_sresults.html', context)

def search_sresults(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = Product.objects.filter(name__icontains=query)

    return render(request, 'search_sresults.html', {'results': results, 'query': query})


def bill_invoice(request):
    # Fetch the latest order for the logged-in user (or implement your logic)
    order = Order.objects.filter(user=request.user).latest('created_at')
    return render(request, 'billinvoice.html', {'order':order})



#drivers view 


# views.py
from django.shortcuts import render, redirect
from .models import Driver

def add_driver(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        license_number = request.POST.get('license_number')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        
        Driver.objects.create(
            name=name,
            license_number=license_number,
            date_of_birth=date_of_birth,
            address=address,
            phone_number=phone_number,
            email=email
        )
        return redirect('add_driver')  # Redirect to the same page after adding a driver

    return render(request, 'add_driver.html')


# views.py
from django.shortcuts import render
from .models import Driver

def view_drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'view_drivers.html', {'drivers': drivers})

def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    if request.method == 'POST':
        driver.delete()
        return redirect('view_drivers')
    return render(request, 'delete_driver.html', {'driver': driver})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Driver
from datetime import datetime

def edit_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    if request.method == 'POST':
        driver.name = request.POST.get('name')
        driver.license_number = request.POST.get('license_number')
        # Convert the date string to the YYYY-MM-DD format
        date_of_birth_str = request.POST.get('date_of_birth')
        date_of_birth = datetime.strptime(date_of_birth_str, '%B %d, %Y').strftime('%Y-%m-%d')
        driver.date_of_birth = date_of_birth
        driver.address = request.POST.get('address')
        driver.phone_number = request.POST.get('phone_number')
        driver.email = request.POST.get('email')
        driver.save()
        return redirect('view_drivers')
    return render(request, 'edit_driver.html', {'driver': driver})


from django.shortcuts import render, redirect
from .models import Technician

def add_technician(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        expertise = request.POST['expertise']
        email = request.POST['email']
        address = request.POST['address']
        Technician.objects.create(
            name=name,
            phone_number=phone_number,
            expertise=expertise,
            email=email,
            address=address
        )
        return redirect('add_technician')
    return render(request, 'add_technician.html')

from django.shortcuts import render
from .models import Technician

def view_technician(request):
    technician = Technician.objects.all()
    return render(request, 'view_technician.html', {'technician': technician})


# from django.shortcuts import render, redirect
# from .models import Product, ProductBooking

# def book_equipment(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         start_date = request.POST.get('start_date')
#         end_date = request.POST.get('end_date')
#         driver_id = request.POST.get('driver_id')
#         technician_id = request.POST.get('technician_id')

#         product = Product.objects.get(pk=product_id)
#         booking = ProductBooking.objects.create(
#             product=product,
#             start_date=start_date,
#             end_date=end_date,
#             driver_id=driver_id if driver_id else None,
#             technician_id=technician_id if technician_id else None
#         )

#         return redirect('booking_confirmation')
#     else:
#         products = Product.objects.filter(availability=True)
#         drivers = Driver.objects.all()
#         technicians = Technician.objects.all()
#         return render(request, 'booking_form.html', {'products': products, 'drivers': drivers, 'technicians': technicians})

# def booking_confirmation(request):
#     return render(request, 'booking_confirmation.html')



from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def book_equipment(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, pk=product_id)
    
    # Get product name
    name = product.name
    
    if request.method == 'POST':
        # Handle form submission
        pass  # Placeholder for handling form submission
    else:
        return render(request, 'booking_form.html', {'product_id': product_id, 'name': name})





# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from .models import ProductBooking,Product

# def book_equipment(request):
#     if request.method == 'POST':
#         # Handle POST request to process form submission
#         name = request.POST.get('name')
#         start_date = request.POST.get('start_date')
#         end_date = request.POST.get('end_date')
#         driver_needed = request.POST.get('driver_needed') == 'yes'
#         technician_needed = request.POST.get('technician_needed') == 'yes'

#         # Assuming you have logic to check if the product name exists
#         # Replace this with your own logic to retrieve the product
#         try:
#             product = Product.objects.get(name=name)
#         except Product.DoesNotExist:
#             return HttpResponse("Product does not exist.")

#         # Create ProductBooking instance
#         product_booking = ProductBooking.objects.create(
#             product=product,
#             start_date=start_date,
#             end_date=end_date,
#             driver_needed=driver_needed,
#             technician_needed=technician_needed
#         )
        
#         # Redirect to a confirmation page or perform any other action
#         return redirect('booking_confirmation')
#     elif request.method == 'GET':
#         # Render the booking form for GET requests
#         return render(request, 'booking_form.html')  # Assuming 'booking_form.html' is the template for the booking form
#     else:
#         # Handle other request methods (e.g., PUT, DELETE)
#         return HttpResponse("Unsupported request method.")
