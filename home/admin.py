from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username','email', 'usertype', 'is_active', 'date_joined')
    list_filter = ('usertype', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'usertype')}),
        ('Permissions', {'fields': ('is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'usertype'),
        }),
    )

#admin.site.register( CustomUserAdmin)
from django.contrib.auth import get_user_model

User = get_user_model()

class SuperuserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return User.objects.filter(is_superuser=False)
    list_display=('email','username')

# Register the custom admin class
admin.site.register(User, SuperuserAdmin)


from django.contrib import admin
from .models import Product, Cart, CartItem


admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)


from django.contrib import admin
from .models import  Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)