from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404
from rest_framework_jwt.settings import api_settings
from django.db.models import F
import beresoon.utils as utils
from beresoon.models import Orders


class OrdersView:

    @staticmethod
    def get_orders(request, id):
        if id is not None:
            ords = Orders.objects.filter(id=id)
        else:
            page = request.GET['page']
            ords = Orders.objects.filter(active=True, ).order_by('register_date')