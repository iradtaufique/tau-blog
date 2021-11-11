from django import template
from blog.models import Post, Comment

register = template.Library()

@register.simple_tag
def count_financial_post():
    return Post.objects.filter(post_category__cat_name='Financial').count()