from django.urls import path
from . import views


urlpatterns = [
    path("", views.apiOverview, name = "api-overview"),
    path("locations-list/", views.locationList, name = "locations-list"),
    path("locations-detail/<str:pk>/", views.locationDetail, name = "locations-detail"),
    path("locations-create/", views.locationCreate, name = "locations-create"),
    path("locations-update/<str:pk>/", views.locationUpdate, name = "locations-update"),
    path("locations-delete/<str:pk>/", views.locationDelete, name = "locations-delete"),  
    path("locations-view/", views.detailView, name = "detail-views"),
       
]
