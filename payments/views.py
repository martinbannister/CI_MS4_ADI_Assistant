from django.shortcuts import render, redirect
import stripe
import json
from django.http import JsonResponse, HttpResponse
from djstripe.models import Product
from django.contrib.auth.decorators import login_required
import djstripe


@login_required
def checkout(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "payments_checkout.html", context)


@login_required
def create_subscription(request):
    if request.method == 'POST':
        # Reads application/json and returns a response
        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)

        try:
            # This creates a new Customer and attaches the PaymentMethod in one API call.
            customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.user.email,
                invoice_settings={
                    'default_payment_method': payment_method
                }
            )

            djstripe_customer = (
                djstripe.models.Customer.sync_from_stripe_data(customer)
            )
            request.user.userprofile.stripeCustomer = djstripe_customer
            request.user.userprofile.stripeCustomerId = customer.id

            # At this point, associate the ID of the Customer object with your
            # own internal representation of a customer, if you have one.
            # print(customer)

            # Subscribe the user to the subscription created
            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[
                    {
                        "price": data["price_id"],
                    },
                ],
                expand=["latest_invoice.payment_intent"]
            )

            djstripe_subscription = (
                djstripe.models.Subscription.sync_from_stripe_data(
                    subscription
                )
            )

            request.user.userprofile.stripeSubscription = djstripe_subscription
            request.user.userprofile.stripeSubscriptionId = subscription.id
            request.user.save()

            return JsonResponse(subscription)
        except Exception as e:
            return JsonResponse({'error': (e.args[0])}, status=403)
    else:
        return HttpResponse('request method not allowed')


def complete(request):
    return render(request, "payment_complete.html")


@login_required
def cancel(request):
    if request.user.is_authenticated:
        sub_id = request.user.userprofile.stripeSubscription.id

    stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY

    try:
        stripe.Subscription.delete(sub_id)
    except Exception as e:
        return JsonResponse({'error': (e.args[0])}, status=403)

    return redirect("home")
