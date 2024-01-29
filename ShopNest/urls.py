from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    # path('admin',views.admin,name='admin'),
    path('',views.index,name='index'),
    path('index.html',views.index),
    path('login.html',views.user_login,name='login'),
    path('register.html',views.register,name='register'),
    path('cart.html',views.cart,name='cart'),
    path('product/<str:brand>/<str:model>/', views.product, name='product'),
    path('profile.html',views.profile,name='profile'),
    path('support.html',views.support,name='support'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('logout',views.user_logout,name='logout'),
    path('cart_order/<str:product_id>/', views.cart_order, name="cart_order"),
    path('support.html', views.support, name='support'),
    path('cart_buy/<str:product_id>', views.cart_buy, name="cart_buy"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
