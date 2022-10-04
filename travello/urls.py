from django.urls import path, include
from . import views
from django_email_verification import urls as email_urls

urlpatterns = [
    path("", views.index, name="index"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('services_d', views.services_d, name="services_d"),
    path('test', views.test, name="test"),
    path("e/<int:id>/", views.single_ott, name="plans"),
    path('planbuy', views.planbuy, name="planbuy"),
    path('contact', views.contact, name="contact"),
    path('destination_details/<int:id>', views.destination_details, name='destination_details'),
    path('booking/<int:id>', views.booking, name="booking"),
    path('receipt', views.receipt, name='receipt'),
    path('search', views.search, name='search'),
    path('confirm_booking', views.confirm_booking, name='confirm_booking'),
    path('orderHistory', views.orderHistory, name="orderHistory"),
    path('email/', include(email_urls)),
    path('delete_destination/<int:id>', views.delete_destination, name="delete_destination"),
    path('plans/', views.plans),
    # path('sortBy', views.sortBy, name="sortBy"),
]