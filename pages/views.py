import stripe
from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings

from profiles.models import UserProfile


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


def index_view(request):
    """ Display current sucscription status """
    try:
        user = UserProfile.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        subscription = stripe.Subscription.retrieve(user.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        context = {
            'subscription': subscription,
            'product': product,
        }

        return render(request, 'index.html', context)

    except stripe.error.CardError as e:
        # Since it's a decline, stripe.error.CardError will be caught

        print('Status is: %s' % e.http_status)
        print('Code is: %s' % e.code)
        # param is '' in this case
        print('Param is: %s' % e.param)
        print('Message is: %s' % e.user_message)
    except stripe.error.RateLimitError as e:
        print('Too many requests made to the API too quickly')
        pass
    except stripe.error.InvalidRequestError as e:
        print("Invalid parameters were supplied to Stripe's API")
        pass
    except stripe.error.AuthenticationError as e:
        print("Authentication with Stripe's API failed")
        print("(maybe you changed API keys recently)")
        pass
    except stripe.error.APIConnectionError as e:
        print("Network communication with Stripe failed")
        pass
    except stripe.error.StripeError as e:
        print("Display a very generic error to the user, and maybe send")
        print("yourself an email")
        pass
    except Exception as e:
        # Something else happened, completely unrelated to Stripe
        print('Non-Stripe Error')
        return render(request, 'index.html')


class SettingsView(TemplateView):
    template_name = 'settings.html'
