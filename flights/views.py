from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingDetailsSerializer, BookingUpdateSerializer


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

class BookingDetails(RetrieveAPIView):
	queryset= Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	look_field = 'id'
	lookup_url_kwarg = 'booking_id'

class BookingUpdate(RetrieveUpdateAPIView):
	queryset= Booking.objects.all()
	serializer_class = BookingUpdateSerializer
	look_field = 'id'
	lookup_url_kwarg = 'booking_id'

class CancelBooking(DestroyAPIView):
	queryset= Booking.objects.all()
	look_field = 'id'
	lookup_url_kwarg = 'booking_id'

