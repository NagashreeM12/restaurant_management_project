from django.shortcuts import render
from django.http import HttpResponse

def add_to_cart(request, item_id):
    cart = request.session.get('cart', [])
    cart.append(item_id)
    request.session['cart'] = cart
    return HttpResponse("Item added to cart")

def cart_count(request):
    cart = request.session.get('cart', [])
    return render(request, 'cart.html', {'cart_count': len(cart)})




