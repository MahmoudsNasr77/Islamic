app_name="Hadiths"
from django.urls import path
from .views import display_hadiths_data, display_hadiths,Home,Bukhari,Muslim,Tirmidhi

urlpatterns = [
    path('', Home, name='Home'),
    path('display_hadiths_data/', display_hadiths_data, name='display_hadiths_data'),
    path('hadith/<int:id>/', display_hadiths, name='display_hadiths'),
    
    path('Bukhari', Bukhari, name='Bukhari'),
        
    path('Muslim', Muslim, name='Muslim'),
    path('Tirmidhi', Tirmidhi, name='Tirmidhi'),
    
    
]
