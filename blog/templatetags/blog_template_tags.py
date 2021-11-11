from django import template
from blog.models import Post, Comment

register = template.Library()

@register.simple_tag
def count_all_post():
    return Post.objects.all().count()

@register.simple_tag
def count_financial_post():
    return Post.objects.filter(post_category='Finance').count()

@register.simple_tag
def count_business_post():
    return Post.objects.filter(post_category='Business').count()


@register.simple_tag
def count_technology_post():
    return Post.objects.filter(post_category='Technology').count()

@register.simple_tag
def count_travel_post():
    return Post.objects.filter(post_category='Travel').count()


@register.simple_tag
def recent_post():
    # recents = Post.objects.all().order_by('-created_at')[:2]
    return Post.objects.all().order_by('-created_at')[:2]