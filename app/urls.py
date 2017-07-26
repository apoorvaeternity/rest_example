from django.conf.urls import url
from .views import UserAuthenticationView, UserRegistrationView , BlogPostView, BlogView

urlpatterns = [
    url(r'^register/', UserRegistrationView.as_view(), name='register'),
    url(r'^login/', UserAuthenticationView.as_view(), name='login'),
    url(r'^blogpost/', BlogPostView.as_view(), name='blogpost'),
    url(r'^blogview/', BlogView.as_view(), name='blogview'),
]