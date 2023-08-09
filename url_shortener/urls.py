from django.urls import path
from . import views

urlpatterns = [
    path('shorten/', views.make_short_url),
    path('<str:short_url>', views.redirect_url)
]