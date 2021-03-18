from django.urls import path
from .views import AllPostView,PostCreateView

urlpatterns = [
    path('',AllPostView.as_view(),name='home'),
    path('new_post/',PostCreateView.as_view(),name='new_post'),
]