import json

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View, generic

import stripe
from core.settings import STRIPE_SECRET

from .models import Item

# Create your views here.
stripe.api_key = STRIPE_SECRET


def get_item(request, pk):
    item = Item.objects.get(id=pk)
    print(item)
    return render(request, "checkout.html", {"item": item})


def create_prod(product):

    prod = stripe.Product.create(
        name=product.name,
        description=product.description,
        default_price_data=dict(currency="PLN", unit_amount=product.price),
    ).to_dict()
    return prod


def buy_item(request, pk):
    item = Item.objects.get(id=pk)
    product = create_prod(item)
    price = product.get("default_price")
    check_out_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price": price,
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url=f"http://127.0.0.1:8000/item/{pk}",
        cancel_url=f"http://127.0.0.1:8000/item/{pk}",
    )
    return JsonResponse(check_out_session)
