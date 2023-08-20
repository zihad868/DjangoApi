from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.BlogList.as_view()),
    path('detail/<int:pk>', views.ApiDetail.as_view()),
    path('contact/', views.contactList.as_view())
]
