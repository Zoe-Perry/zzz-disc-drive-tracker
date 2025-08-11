from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.CharacterList.as_view(), name='home'),
    path('character_detail/<int:character_id>/', views.character_detail, name='character_detail'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)