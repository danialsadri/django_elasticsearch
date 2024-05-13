from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book/detail/<int:book_id>/<slug:book_slug>/', views.BookDetailView.as_view(), name='book_detail'),
]
