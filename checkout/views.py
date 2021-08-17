from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Theres's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51JPP4CCEcerLqohRAkvc5BrsvhzH4U88DjL9jfqMqSjj1AVcQseQy0HvR37KfuUQBL72CPyiGpVaIK6AmKHsf2Fz00H04ZaYJa',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

