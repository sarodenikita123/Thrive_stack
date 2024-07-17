from django.urls import path
from .views import manageview, show, update, delete


urlpatterns = [
    path('a1/', manageview),
    path('show/', show),
    path("update/", update),
    path("delete/", delete)

]