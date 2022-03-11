from django.contrib import admin
from django.urls import path

from table import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeListView.as_view(), name='home'),
]
