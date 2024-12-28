from django.urls import path
from . import views

urlpatterns = [
  path("", views.readCreate, name="index"),
  path('update/<int:pk>/', views.updateItem, name="update"),
  path("delete/<int:pk>/", views.deleteItem, name='delete')
]