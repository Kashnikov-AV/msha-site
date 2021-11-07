from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        products = [0,1,2,3,4,5,6]
        catalog_list = ['Овощи','Фрукты','Молочные продукты','Ягоды',
                        'Продукты пчеловодства','Рассада','Цветы и декоративные расстения']

        return render(request, 'base/index.html', {'catalog_list': catalog_list,
                                                   'products': products})