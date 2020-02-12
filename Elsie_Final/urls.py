"""Elsie_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from products import views as product_views
from carts import views as cart_views
from orders import views as order_views
from accounts import views as accounts_views
from marketing import views as marketing_views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/logout/', accounts_views.LogOutView, name='auth_logout'),
    path('accounts/login/', accounts_views.LogInView, name='auth_login'),
    path('accounts/register/', accounts_views.RegisterView, name='auth_register'),
    path('accounts/address/add/', accounts_views.AddUserAddress, name='add-user-address'),
    path('', product_views.home, name='home'),
    path('s/', product_views.search, name='search'),
    path('items/', product_views.all, name='items'),
    path('cart/', cart_views.ViewCart, name='cart'),
    path('checkout/', order_views.Checkout, name='checkout'),
    path('orders/', order_views.Orders, name='user-orders'),
    
    path('cart/<id>\d+/$', cart_views.RemoveFromCart, name='remove-from-cart'),
    path('cart/<slug:slug>/', cart_views.AddToCart, name='add-to-cart'),
    path('items/<slug:slug>/', product_views.single, name='single-item'),
    path('accounts/activate/<str:activation_key>', accounts_views.ActivationView, name='activate'),
    path('ajax/dismiss_marketing_message/', marketing_views.DismissMarketingMessage, name='dismiss-marketing-message'),
    path('ajax/email_signup/', marketing_views.EmailSignUp, name='ajax_email_signup'),
    path('ajax/add-user-address/', accounts_views.AddUserAddress, name='ajax-add-user-address'),


    #(?P<all_items>.*)
    #(?P<all_items>\d+)
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
