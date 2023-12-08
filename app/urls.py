from django.urls import path
from . import views
 
app_name="app"

urlpatterns = [
    path('', views.index,name="index"),
    path('remove_bg/', views.remove_bg, name='upload_image'),
]
