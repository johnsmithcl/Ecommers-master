from django.shortcuts import render,redirect,get_object_or_404
from app1.models import product
from .models import cart,cartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def _cart_id(request):
    cart= request.session.session_key
    if not cart:
        cart= request.session.create()
    return cart

def add_cart(request,product_id):
    Product = product.objects.get(id=product_id)
    try:
        Cart = cart.objects.get(cart_id=_cart_id(request))
    except cart.DoesNotExist:
        Cart = cart.objects.create(cart_id=_cart_id(request))
        Cart.save()
    try:
        cart_item=cartItem.objects.get(product=Product,cart=Cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+=1
        cart_item.save()
    except cartItem.DoesNotExist:
        cart_item=cartItem.objects.create(product=Product,quantity=1,cart=Cart)
        cart_item.save()
    return redirect('cart:cart_details')

def cart_details(request,total=0,counter=0,cart_item=None):
    try:
        Cart = cart.objects.get(cart_id=_cart_id(request))
        cart_item = cartItem.objects.filter(cart=Cart,active=True)
        for ci in cart_item:
            total+=ci.product.price * ci.quantity
            counter+=ci.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_item=cart_item, total=total, counter=counter))

def remove_cart(request,product_id):
    Cart = cart.objects.get(cart_id=_cart_id(request))
    Product = get_object_or_404(product,id=product_id)
    cart_item = cartItem.objects.get(product=Product, cart=Cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_details')

def delete_cart(request,product_id):
    Cart = cart.objects.get(cart_id=_cart_id(request))
    Product = get_object_or_404(product,id=product_id)
    cart_item = cartItem.objects.get(product=Product, cart=Cart)
    cart_item.delete()
    return redirect('cart:cart_details')

