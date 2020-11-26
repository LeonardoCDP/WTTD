from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription


new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmação de inscrição')


def detail(request, hashid):
    try:
        subscription = Subscription.objects.get(hashid=hashid)
    except (Subscription.DoesNotExist, ValidationError):
        raise Http404
    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})


