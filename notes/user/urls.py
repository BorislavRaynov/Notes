from django.urls import path

from .views import home_page, profile_details, delete_profile


urlpatterns = [
    path('', home_page, name='home-page'),
    path('profile/', profile_details, name='profile-details'),
    path('profile/delete/', delete_profile, name='delete-profile')
]