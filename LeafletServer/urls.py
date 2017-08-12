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

from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from LeafletServer.google_login.views import GoogleLogin
#from LeafletServer.facebook_login.views import FacebookLogin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authentication import get_authorization_header
from graphene_django.views import GraphQLView
from jwt_auth.mixins import JSONWebTokenAuthMixin

admin.autodiscover()

class OptionalJWTMixin(JSONWebTokenAuthMixin):
    """
    Optional JWT Mixin
    """
    def dispatch(self, request, *args, **kwargs):
        auth = get_authorization_header(request)
        print(auth)
        if auth:
            return super(OptionalJWTMixin, self).dispatch(request, *args,
                                                          **kwargs)
        return super(JSONWebTokenAuthMixin, self).dispatch(request, *args,
                                                           **kwargs)

class AuthGraphQLView(OptionalJWTMixin, GraphQLView):
    """
    Auth Graph QL
    """
    pass

urlpatterns = [
    url(r'^graphql', csrf_exempt(AuthGraphQLView.as_view())),
    url(r'^graphiql', include('django_graphiql.urls')),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    #url(r'^accounts/', include('allauth.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^auth/google/$', GoogleLogin.as_view(), name='google_login'),
    url(r'^graphql', csrf_exempt(AuthGraphQLView.as_view())),
    url(r'^graphiql', include('django_graphiql.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
