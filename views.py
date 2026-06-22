from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('product_list')

def cart_view(request):
    cart_items = CartItem.objects.all()
    # Ella items-oda total price-ai kootum
    grand_total = sum(item.total_price for item in cart_items)
    
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total
    })

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_view')