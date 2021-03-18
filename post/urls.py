from django.urls import path
from .views import AllPostView,PostCreateView,PostDetailView

urlpatterns = [
    path('',AllPostView.as_view(),name='home'),
    path('new_post/',PostCreateView.as_view(),name='new_post'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='detail')
]