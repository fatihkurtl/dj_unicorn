from django.urls import path, include
from . import views

urlpatterns = [
    path("unicorn/", include("django_unicorn.urls")),
    path("", views.HomePageView.as_view(), name="index"),
]