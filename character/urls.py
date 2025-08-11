from . import views
from django.urls import path

urlpatterns = [
    path('',views.CharacterList.as_view(), name='home'),
    path('character_detail/<int:character_id>/', views.character_detail, name='character_detail'), 
]