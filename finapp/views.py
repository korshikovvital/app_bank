from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Product,Category
from .forms import *
from django.views.generic import ListView,DetailView,CreateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# def homepage(requests):
#     product=Product.objects.all()
#     return render(requests,'finapp/index.html',{'product':product})

class Homepage(ListView):
    model=Product
    template_name = 'finapp/index.html'
    context_object_name = 'product'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.order_by('-profit')



# def get_category(requests,cat_slug):
#     cat_get = Category.objects.get(url=cat_slug)
#     product=Product.objects.filter(category__url=cat_slug)
#
#     cat_selected = cat_slug
#     return render(requests, 'finapp/category.html', {'cat_get':cat_get,'cat_selected':cat_selected,'product':product})

class Get_category(ListView):
    '''Категории'''
    model = Product
    template_name = 'finapp/category.html'
    context_object_name = 'product'
    slug_field = 'category__url'
    slug_url_kwarg ='cat_slug'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__url=self.kwargs['cat_slug']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['cat_selected']=self.kwargs['cat_slug']
        return context








# def get_product(requests,pro_id):
#     product=Product.objects.get(id=pro_id)
#
#     return render(requests,'finapp/product.html',{'product':product})


class Get_product(DetailView):
    model = Product
    template_name = 'finapp/product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pro_id'


# def addform(requests):
#     if requests.method=='POST':
#         form=AddProductForm(requests.POST,requests.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form=AddProductForm()
#     return render(requests,'finapp/add_form.html',{'form':form})

class Addform(LoginRequiredMixin,CreateView):
    '''Форма продукта'''
    form_class = AddProductForm
    template_name = 'finapp/add_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

class UserRegisret(CreateView):
    '''Форма регистрации'''
    form_class = UserRegisterForm
    template_name = 'finapp/register.html'
    # success_url = reverse_lazy('login')

    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return redirect('home')


class UserLogin(LoginView):
    '''Форма логина'''
    form_class = AuthenticationForm
    template_name = 'finapp/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def user_logout(requests):
    logout(requests)
    return redirect('login')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'finapp/contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')



