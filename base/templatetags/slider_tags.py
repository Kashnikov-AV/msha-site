from django import template
from base.models import Slider

register = template.Library()

@register.inclusion_tag('base/slider.html')
def block_slider():
    #slider query_sets
    slider_block = Slider.objects.all()
    return {'slider_block': slider_block}