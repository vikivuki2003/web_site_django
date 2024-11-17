from django.shortcuts import render, get_object_or_404

from cart.cart import Cart
from shop.models import ProductProxy, Product
from django.http import JsonResponse


def cart_view(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/cart_view.html', context)

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(ProductProxy, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_qty = cart.__len__()
        response = JsonResponse({'product': product.title, 'qty': cart_qty})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)

        cart_qty = cart.__len__()

        cart_total = cart.get_total_price()
        response = JsonResponse({'qty': cart_qty, 'total': cart_total})
        return response

def cart_update(request):
    ...

