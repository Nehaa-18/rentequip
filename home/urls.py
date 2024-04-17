from django.contrib import admin
from django.urls import path,include
from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index,name='home'),
    path('index.html', views.index,name='home'),
    path('login.html', views.login,name='login'),
    path('registration', views.registration,name='registration'),
    path('about.html', views.about,name='about'),
    path('contact.html', views.contact,name='contact'),
    
   
    path('index',views.index,name="index"),
    path('admindash',views.admindash,name="admindash"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('dashboardOrg',views.dashboardOrg,name="dashboardOrg"),
    path('account',views.account,name="account"),
    path('order',views.order,name="order"),
    path('addequip',views.addequip,name="addequip"),
    path('view_equip',views.view_equip,name="view_equip"),
    path('usertypecount', views.usertypecount, name='usertypecount'),
    path('wishlist',views.wishlist,name="wishlist"),
    # Add a product to the wishlist
   
    path('rent',views.rent,name="rent"),
    path('accountorg',views.accountorg,name="accountorg"),
    #path('logout/', views.logout_view, name='logout'),

    path('regusers', views.regusers, name='regusers'),
    path('cusers', views.cusers, name='cusers'),

    #categories
    path('movingequip',views.movingequip,name="movingequip"),

    #path('admin_index/', views.admin_index, name='admin_index'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),


    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    #path('product/<int:product_id>/', views.product, name='product'),


    path('user_profile',views.user_profile,name="user_profile"),



    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
    #path('accounts/login/', views.login, name='login'),
    #path('accounts/registration/', views.registration, name='registration'),
    path('logout',views.logout,name="logout"),


   
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
   

    path('movingequip', views.movingequip, name='movingequip'),
    path('officeequip', views.officeequip, name='officeequip'),
    path('dumpsterequip', views.dumpsterequip, name='dumpsterequip'),
    path('sportsequip', views.sportsequip, name='sportsequip'),
    path('audioequip', views.audioequip, name='audioequip'),
    path('visualequip', views.visualequip, name='visualequip'),

    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('search/', views.search_products, name='search_products'),
    path('product', views.product, name='product'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('cart', views.view_cart, name='cart'),
    path('increase-cart-item/<int:product_id>/', views.increase_cart_item, name='increase-cart-item'),
    path('decrease-cart-item/<int:product_id>/', views.decrease_cart_item, name='decrease-cart-item'),
    path('fetch-cart-count/', views.fetch_cart_count, name='fetch-cart-count'),


    path('fetch-cart-count/', views.fetch_cart_count, name='fetch-cart-count'),
    path('create-order/', views.create_order, name='create-order'),
    path('handle-payment/', views.handle_payment, name='handle-payment'),
    path('checkout/', views.checkout, name='checkout'),

    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order_list', views.order_list, name='order_list'),

    path('search_blog', views.search_blog, name='search_blog'),
    path('search_results', views.search_results, name='search_results'),

    path('search_mov', views.search_mov, name='search_mov'),
    path('search_sports', views.search_sports, name='search_sports'),
    path('search_audio', views.search_audio, name='search_audio'),
    path('search_dum', views.search_dum, name='search_dum'),
    path('search_visual', views.search_visual, name='search_visual'),
    path('search_office', views.search_office, name='search_office'),
    path('search_mresults', views.search_mresults, name='search_mresults'),
    path('search_oresults', views.search_oresults, name='search_oresults'),
    path('search_aresults', views.search_aresults, name='search_aresults'),
    path('search_dresults', views.search_dresults, name='search_dresults'),
    path('search_vresults', views.search_vresults, name='search_vresults'),
    path('search_sresults', views.search_sresults, name='search_sresults'),

    path('billinvoice/', views.bill_invoice, name='bill_invoice'),


    path('add_driver/', views.add_driver, name='add_driver'),
    path('view_drivers/', views.view_drivers, name='view_drivers'), 
    path('delete_driver/<int:driver_id>/', views.delete_driver, name='delete_driver'),
    path('edit_driver/<int:driver_id>/', views.edit_driver, name='edit_driver'),

    
    path('add_technician/', views.add_technician, name='add_technician'),
    path('view-technician/', views.view_technician, name='view_technician'),

 
    path('book/', views.book_equipment, name='book_equipment'),
    # path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

