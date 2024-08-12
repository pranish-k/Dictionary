from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('submit/',views.submit, name='submit'),
    path('update/<str:pk>', views.update, name='update' ),

]