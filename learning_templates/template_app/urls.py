from django.urls import path
from template_app import views

# for template tagging, set global name app_name to the name of your app
app_name = 'template_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
