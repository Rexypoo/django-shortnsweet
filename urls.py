from django.urls import path

from . import views

app_name = 'shortnsweet'
urlpatterns = [
    path('<slug:short_name>', views.redirect_alias, name='short-name'),
]
