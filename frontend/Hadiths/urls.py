app_name="Hadiths"
from django.urls import path
from .views import display_hadiths_data, display_hadiths

urlpatterns = [
    path('', display_hadiths_data, name='display_hadiths_data'),
    path('hadith/<int:id>/', display_hadiths, name='display_hadiths'),
]
