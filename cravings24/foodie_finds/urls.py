from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('reg',views.reg,name='reg'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collectionsview,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.product_details,name='product_details'),
    path('addtobag',views.add_to_bag,name="addtobag"),
    path('bag',views.bag_page,name="bag"),
    path('remove_bag/<str:cid>',views.remove_bag,name="remove_bag"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
]
