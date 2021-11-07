from django.shortcuts import render
from django.views import View
from base.models import Product

class Index(View):
    def get(self, request):
        products = Product.objects.all()
        catalog_list = ['Овощи','Фрукты','Молочные продукты','Ягоды',
                        'Продукты пчеловодства','Рассада','Цветы и декоративные расстения']

        return render(request, 'base/index.html', {'catalog_list': catalog_list,
                                                   'products': products})