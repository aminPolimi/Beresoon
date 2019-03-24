# from django.views import View
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404
from rest_framework_jwt.settings import api_settings
import beresoon.utils as utils


class UserView:

    @staticmethod
    def login(request):
        # res = request.data
        # # print(res)
        # user = authenticate(username=res['username'], password=res['password'])
        # if user is None:
        #     raise PermissionDenied()
        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # payload = jwt_payload_handler(user)
        # token = jwt_encode_handler(payload)
        #
        # return HttpResponse(utils.json_dumps_nan({'token': token, 'user': {'id': user.id, 'name': user.username},
        #                                           'email': user.email}), content_type="application/json")

        return HttpResponse(utils.json_dumps_nan({}), content_type="application/json")
