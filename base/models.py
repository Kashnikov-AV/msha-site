from django.db import models
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Slider(models.Model):
    name = models.CharField(max_length=100, verbose_name='номер слайда начиня с 0 по порядку')

    title = models.CharField(max_length=180, verbose_name='заголовок на слайде')

    description = models.CharField(max_length=500, verbose_name='добваить описание')

    img = models.ImageField(blank=False, upload_to='slider/', verbose_name='добавить изобрадение')

    class Meta:
        verbose_name = 'слайд'

        verbose_name_plural = 'слайды'

    def __str__(self):
        return self.name

CATEGORY_CHOICES = (
    ('Vegetables', 'Овощи'),
    ('Fruit', 'Фрукты'),
    ('Dairy_products', 'Молочные продукты'),
    ('Berries', 'Ягоды'),
    ('Beekeeping_Products', 'Продукты пчеловодства'),
    ('Seedling', 'Рассада'),
    ( 'Flowers_plants', 'Цветы и декоративные расстения'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название продукта')

    price = models.FloatField(verbose_name='цена')

    img = models.ImageField(blank=False, upload_to='slider/', verbose_name='добавить изобрадение')

    category = models.CharField(max_length=30,choices=CATEGORY_CHOICES, verbose_name='категория продукта', default='Vegetables')

    class Meta:
        verbose_name = 'товар'

        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name

'''
@receiver(pre_delete, sender=Slider)
def slider_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.img.delete(False)

@receiver(pre_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.img.delete(False)
'''


