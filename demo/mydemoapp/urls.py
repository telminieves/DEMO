from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("newhome", views.newhome, name = "newhome"),
    path("plotly", views.plotly_view, name = "plotly"),
    path("jinja", views.jinja_view, name = "jinja")
    ]