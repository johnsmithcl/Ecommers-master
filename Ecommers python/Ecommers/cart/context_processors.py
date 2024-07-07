from .models import cart,cartItem
from .views import _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            Cart=cart.objects.filter(cart_id=_cart_id(request))
            cart_items=cartItem.objects.all().filter(cart=Cart[:1])
            for i in cart_items:
                item_count+=i.quantity
        except cart.DeosNotExist:
            item_count=0
    return dict(item_count=item_count)

