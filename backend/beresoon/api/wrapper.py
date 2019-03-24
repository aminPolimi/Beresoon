from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from beresoon.views import UserView
from beresoon.tests import OrdersTest


@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    return UserView.login(request)


@api_view(['GET'])
@permission_classes((AllowAny,))
def orders(request, id=None):
    print(request, id)
    return UserView.login(request)


@api_view(['GET'])
@permission_classes((AllowAny,))
def test(request):
    return OrdersTest.orders(request)