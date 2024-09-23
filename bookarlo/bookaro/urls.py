from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from .views import BookTicketView, CancelBookingView, CreateEventView, CreateLocationView, EventDetailView, EventListView, LogoutView, RegisterView, UserBookingsView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('book-ticket/', BookTicketView.as_view(), name='book-ticket'),
    path('bookings/', UserBookingsView.as_view(), name='user-bookings'),
    path('cancel-booking/<int:booking_id>/', CancelBookingView.as_view(), name='cancel-booking'),
    path('create-event/', CreateEventView.as_view(), name='create-event'),
    path('create-location/', CreateLocationView.as_view(), name='create-location'),
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]
