from django.db import models

class Hadith (models.Model):
    HadithsNarrator=[
    ('البخاري','البخاري'),
    ('مسلم','مسلم'),
    ('الترمذي','الترمذي'),
]
    narrator=models.CharField(max_length=250,choices=HadithsNarrator)
    text=models.TextField(max_length=5000)
    explantion=models.TextField(max_length=5000,blank=True)
