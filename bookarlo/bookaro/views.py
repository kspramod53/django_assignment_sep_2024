from django.shortcuts import render

# Create your views here.

# yourapp/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsEventManager

from .serializers import EventSerializer, LocationSerializer, RegisterSerializer

# bookaro/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Event, Booking
from .serializers import BookingSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class EventManagerView(APIView):
    permission_classes = [IsAuthenticated, IsEventManager]

    def get(self, request):
        # Your logic for event manager
        return Response({"message": "Hello, Event Manager!"})
    
class BookTicketView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        event_id = request.data.get("event_id")
        tickets = request.data.get("tickets")

        try:
            event = Event.objects.get(id=event_id)
            if event.available_tickets >= tickets:
                booking = Booking.objects.create(
                    user=request.user, event=event, tickets_booked=tickets
                )
                event.available_tickets -= tickets
                event.save()
                return Response(
                    BookingSerializer(booking).data, status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"error": "Not enough tickets available"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Event.DoesNotExist:
            return Response(
                {"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        
class UserBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class CancelBookingView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id, user=request.user)
            event = booking.event
            event.available_tickets += booking.tickets_booked
            event.save()
            booking.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Booking.DoesNotExist:
            return Response({"error": "Booking does not exist"}, status=status.HTTP_404_NOT_FOUND)


class CreateEventView(generics.CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsEventManager]  

class CreateLocationView(generics.CreateAPIView):
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated, IsEventManager]  


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'location']                





