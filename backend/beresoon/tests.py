from django.test import TestCase
from django.http import HttpResponse, Http404
from rest_framework_jwt.settings import api_settings
import beresoon.utils as utils

class OrdersTest:

    @staticmethod
    def orders(request):
        dt = {'id':1, 'register_date':'2019-03-15 10:26', 'price': 100, 'currency':'$', 'quantity':2,
              'unit': '', 'from':'Milan-IT', 'to':'Tehran-IR', 'user':'Amin', 'trip':'2019-04-15',
              'shipment':10}
        return HttpResponse(utils.json_dumps_nan(dt), content_type="application/json")


