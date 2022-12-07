from django.urls import path, include

urlpatterns = [
    path('', include('log.urls')),
    path('', include('root.urls')),
]
