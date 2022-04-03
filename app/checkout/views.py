from oscar.apps.checkout.views import *


class PaymentDetailsView(PaymentDetailsView):
    template_name = 'payment_details.html'
    preview = False


class ThankYouView(ThankYouView):
    template_name = 'thank_you.html'
