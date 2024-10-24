from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'accounts'
urlpatterns = [
    path('register/' ,views.UserRegister.as_view()),
    path('profile/', views.ProfileApi.as_view(), name="profile"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('addscore/', views.AddScoreView.as_view(), name='add_score'),
    path('allprofiles/', views.AllProfilesView.as_view(), name='allprofiles'),
]
