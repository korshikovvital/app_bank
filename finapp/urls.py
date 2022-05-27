
from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [

    path('',cache_page(60)(Homepage.as_view()),name='home'),
    path('category/<slug:cat_slug>/',Get_category.as_view(),name='get_category'),
    path('product/<int:pro_id>/',Get_product.as_view(),name='get_product'),
    path('addform/',Addform.as_view(),name='addform'),
    path('register/',UserRegisret.as_view(),name='register'),
    path('login/',UserLogin.as_view(),name='login'),
    path('logout/',user_logout,name='logout'),
    path('contact/',ContactFormView.as_view(),name='contact'),



]
