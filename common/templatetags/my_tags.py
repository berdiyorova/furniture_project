from django import template

register = template.Library()

@register.simple_tag
def get_full_url(request, lang):
    url = request.path.split('/')
    url[1] = lang
    return '/'.join(url)

@register.filter
def in_cart(request, pk):
    return pk in request.session.get('cart', [])

@register.filter
def in_wishlist(request, pk):
    return pk in request.session.get('wishlist', [])

