from django.urls import path, include
from knox import views as knox_views
from Accounts.api import RegistrationAPI, LoginAPI, GetUser
# from .views import ProfileView, Updateprofile
# ProfileViewSet ProfileDetails


app_name = 'Accounts'
# router = routers.DefaultRouter()
# # router.register('api/profiles', ProfileViewSet, "profiles")
# router.register('api/user/(?P<user_id>\d+)/profile', Profile,"profile")
# router.register('api/profile', Profile,"profile")


urlpatterns = [
    # path("updateprofile/", Updateprofile.as_view(), name="updateprofile"),
    # path("profile/", ProfileView.as_view(), name="profile"),
    path('auth', include('knox.urls')),
    path('register', RegistrationAPI.as_view(), name='register'),
    path('login', LoginAPI.as_view(), name='login'),
    path('user', GetUser.as_view(), name='user'),

    path('logout', knox_views.LogoutView.as_view(), name='knox_logout')
]
# urlpatterns += router.urls
# urlpatterns
