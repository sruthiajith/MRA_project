from django.contrib import admin
from django.urls import path
from MovieRecommender import views
from django.conf import settings
from django.conf.urls.static import static
app_name='MovieRecommender'

urlpatterns = [


    path('signup/',views.signup,name="signup"),
    path('login/',views.user_login,name="login"),
    path('home/',views.home,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addmovie/',views.addmovie,name="addmovie"),
    path('logout/',views.user_logout,name="logout"),
    path('profile/',views.profile,name="profile"),

]