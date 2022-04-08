from django.shortcuts import render, redirect
import stripe
import json
from django.http import JsonResponse
from djstripe.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "payments_checkout.html", context)
