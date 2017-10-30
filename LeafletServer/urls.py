"""LeafletServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url, static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
#from LeafletServer.facebook_login.views import FacebookLogin
from LeafletServer.google_login.views import GoogleLogin
from rest_framework.urlpatterns import format_suffix_patterns
from graphene_django.views import GraphQLView
from jwt_auth.mixins import JSONWebTokenAuthMixin
from rest_framework_jwt.views import verify_jwt_token, obtain_jwt_token, \
    refresh_jwt_token

admin.autodiscover()

class AuthGraphQLView(JSONWebTokenAuthMixin, GraphQLView):
    """
    Auth GraphQL View
    """
    pass

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^auth/google/$', GoogleLogin.as_view(), name='google_login'),
] + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [url(r'^graphql', csrf_exempt(AuthGraphQLView.as_view(
        graphiql=True)))]
else:
    urlpatterns += [url(r'^graphql', csrf_exempt(AuthGraphQLView.as_view(
        graphiql=False)))]

urlpatterns = format_suffix_patterns(urlpatterns)
