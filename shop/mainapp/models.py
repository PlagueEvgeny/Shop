from django.db import models

from authapp.models import MyUser


class Category(models.Model):
    name = models.CharField(verbose_name='название категории', max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категорий'


class Product(models.Model):
    title = models.CharField(verbose_name='заголовок', max_length=128)
    desc = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='цена товара', max_digits=6, decimal_places=2)
    photo = models.ImageField(verbose_name='фото', upload_to='product/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'товар'
        verbose_name_plural = 'товаров'


class Order(models.Model):
    user = models.ForeignKey(Profile, verbose_name='пользователь', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, verbose_name='товар', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.login

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

