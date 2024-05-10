from django.urls import path

from detaile_app import views
from django.conf import settings
from django.conf.urls.static import static
app_name='detaile_app'

urlpatterns = [

      path("movieDetail/<int:movie_id>/",views.movieDetail,name="movieDetail"),
      path("SearchResult/",views.SearchResult,name="SearchResult"),
]