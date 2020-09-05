from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from .models import Product
from .models import CartItem

# Create your views here.
# /products -> index
# Uniform Resource Locator (Address)
def index(request):
  #The button to add items to the cart
  if (request.GET.get("add-cart")):
    name = request.GET.get("product-name")
    price = request.GET.get("product-price")
    quantity = request.GET.get("product-count")
    if (CartItem.objects.filter(name=name).count()) == 0:
      cart_item = CartItem.objects.create(name=name, price=float(price), quantity=quantity)
      cart_item.save()
    else:
      CartItem.objects.filter(name=name).update(quantity=quantity)

  items = CartItem.objects.all()
  count = 0

  for i in items:
    count += i.quantity

  products = Product.objects.all()

  #The search logic
  if (request.GET.get("search-submit")):
    phrase = request.GET.get("search-entry")
    all_products = products
    products = []
    for p in all_products:
      if phrase.lower() in p.name.lower():
        products.append(p)

  return render(request, 'index.html', {'products': products, 'cart_size': count})


def new(request):
  if (request.GET.get("submit")):
    name = request.GET.get("name_input")
    price = request.GET.get("price_input")
    stock = request.GET.get("stock_input")

    product = Product.objects.create(name=name, price=float(price), stock=int(stock))
    product.save()

  return render(request, 'new_product.html')

def view_cart(request):
  items = CartItem.objects.all()
  price = 0.0

  for i in items:
    price += i.price

  return render(request, 'view_cart.html', {'items': items, 'total': price})

def order_placed(request):
  CartItem.objects.all().delete()
  return render(request, 'order_placed.html')


