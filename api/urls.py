from django.urls import path

from api import views


app_name = "api"
urlpatterns = [
    path('locations/all/', views.GeoListView.as_view({'get': 'list'}), name='locations-list'),
    path('locations/create/', views.GeoListView.as_view({'post': 'create'}), name='locations-create'),
    path('locations/delete/<int:geo_id>/', views.GeoListView.as_view({'delete': 'destroy'}), name='locations-delete'),
]
