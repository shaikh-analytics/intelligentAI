from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service_detail',views.service_detail,name='service_detail'),
    path('portfolio/',views.portfolio,name='portfolio')
]
