from django.urls import path
from .views import AllPostView

urlpatterns = [
    path('',AllPostView.as_view(),name='home')
]