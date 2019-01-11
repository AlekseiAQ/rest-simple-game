from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from game import views

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"profiles", views.ProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include(router.urls)),
    url(r"^rest-auth/", include("rest_auth.urls")),
    url(r"^rest-auth/registration/", include("rest_auth.registration.urls")),
]
