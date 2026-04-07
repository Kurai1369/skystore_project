from django.urls import path
from . import views

app_name = 'catalog'  # пространство имён для URL

urlpatterns = [
    path('', views.home, name='home'),           # главная страница
    path('contacts/', views.contacts, name='contacts'),  # контакты
]