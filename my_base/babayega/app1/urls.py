from . import views
from django.urls import path

urlpatterns =[
    path('', views.ProfileView.as_view(), name='profile'),
    path('contact_me', views.contact_me, name='contact_me'),
    path('dashboard/', views.DashboardView.as_view(), name='Dashboard'),
    path('phone_number/<int:pk>', views.ContactDetailView.as_view(), name='phone_number_detail'),
    path('phone_number/', views.ContactListView.as_view(), name='phone_number'),
    path('phone_number/new', views.ContactCreateView.as_view(), name='phone_number_new'),
    path('phone_number/<int:pk>/edit', views.ContactUpdateView.as_view(), name='phone_number_edit'),
    path('phone_number/<int:pk>/remove', views.ContactDeleteView.as_view(), name='phone_number_remove'),
]