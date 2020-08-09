from django.urls import path, include
from . import views
from rest_framework import routers
#routers helps us to create get and post request

router= routers.DefaultRouter()
router.register('Activity_Period',views.ActivityView)

urlpatterns = [
    path('', include(router.urls)),
    
]
