from django.db import models
from django.urls import reverse


class Category(models.Model):
    ''''Категории'''
    name=models.CharField(max_length=100)
    published=models.BooleanField(default=True)
    url=models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('get_category',kwargs={'cat_slug':self.url})

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

class Product(models.Model):
    '''Продукты'''
    name=models.CharField(max_length=100,verbose_name='Имя')
    category=models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name='Категория')
    image=models.ImageField(upload_to='photo/%y/%d/%m',verbose_name='Фото')
    descriptions=models.TextField(verbose_name='Описание')
    info=models.TextField(null=True,verbose_name='Информация')
    profit=models.SmallIntegerField(verbose_name='Доход')
    link=models.CharField(max_length=100,verbose_name='Ссылка')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('get_product',kwargs={'pro_id':self.pk})

    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'



