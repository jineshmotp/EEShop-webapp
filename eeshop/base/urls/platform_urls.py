from django.urls import path
from base.views import platform_views as views

urlpatterns = [
  
    path('',views.getPlatformdatas,name="platforms"),
    path('create/<str:pk>/',views.createPlatform,name="platform-create"), 
    path('<str:platk>/',views.getPlatformdata,name="platform"),
    path('platformdetails/<str:pk>/',views.getPlatformDetails,name="platform-details"),
   
    path('delete/<str:pk>/',views.deletePlatform,name="platform-delete"), 
    path('update/<str:pk>/',views.updatePlatform,name="platform-update"), 
    
]