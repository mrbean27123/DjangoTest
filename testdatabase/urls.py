from django.urls import path

from . import views

urlpatterns = [
    path('', views.testdatabase_main, name='testdatabase_main'),
    path('add', views.testdatabase_add_movie, name='add_movie'),
    path('<int:pk>', views.MovieDetailView.as_view(), name='get_movie'),
    path('<int:pk>/update', views.MovieUpdateView.as_view(), name='update_movie'),
    path('<int:pk>/delete', views.MovieDeleteView.as_view(), name='delete_movie'),
]
