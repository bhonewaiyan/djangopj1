from django.urls import path
from .import views
urlpatterns = [
	path('bbq', views.bbq, name='bbq',)


]