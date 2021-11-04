from django.shortcuts import render
from django.views import View

class Blog(View):
    def get(self, request):
        return render(request, 'blog/blog.html')