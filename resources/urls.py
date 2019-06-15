from resources import views
from django.urls import path

urlpatterns = [
    path('', views.ItemList.as_view()),
    path('/<int:pk>', views.ItemObject.as_view())
]
