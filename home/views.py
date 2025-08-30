# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

# View to handle adding an item to the cart
def add_to_cart(request, item_id):
    # Retrieve the current cart from the session (empty list if not present)
    cart = request.session.get('cart', [])
    
    # Add the new item to the cart
    cart.append(item_id)
    
    # Save the updated cart back to the session
    request.session['cart'] = cart
    
    # Redirect to the cart count view after adding an item
    return redirect('cart_count')  # Adjust this as per your URL name

# View to display the cart count (total number of items)
def cart_count(request):
    # Get the total number of items in the cart
    cart = request.session.get('cart', [])
    cart_count = len(cart)  # Count the number of items in the cart
    
    # Render the homepage template with the cart count
    return render(request, 'index.html', {'cart_count': cart_count})





