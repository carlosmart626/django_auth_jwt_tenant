from django.conf.urls import url
from django.views import View
from django.http import HttpResponse
from django_auth_jwt_tenant.mixins import JSONWebTokenTenantAuthMixin


class MyView(JSONWebTokenTenantAuthMixin, View):
    def get(self, request):
        # <view logic>
        return HttpResponse('OK')


urlpatterns = [
    url(r'^api/', MyView.as_view()),
]