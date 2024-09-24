# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git@github.com:kspramod53/django_assignment_sep_2024.git
    $ cd django_assignment_sep_2024
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:
    $ cd bookarlo

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver


Endpoints:

POST /register/

1.
{
    "email": "user@example.com",
    "password": "password123",
    "first_name": "John",
    "last_name": "Doe",
    "role": "User"
}
2.
{
    "email": "user@example.com",
    "password": "password123",
    "first_name": "John",
    "last_name": "Doe",
    "role": "Event Manager"
}

Login

Endpoint: POST /api/token/

{
    "email": "user@example.com",
    "password": "password123"
}

Create Location

Endpoint: POST /create-location/
Authorization : Event manager access token
{
    "name": "Stadium",
    "address": "123 Main St, Anytown, USA"
}


Create Event (Event Manager Role)

Endpoint: POST /create-event/

{
    "title": "Concert",
    "description": "Live music concert",
    "date": "2023-12-25",
    "time": "18:00:00",
    "location": 1, 
    "total_tickets": 100,
    "available_tickets": 100,
    "payment_options": "Credit Card, PayPal"
}

Book Ticket

Endpoint: POST /book-ticket/
Authorization : bearer acess token
{
    "event_id": 1,  
    "tickets": 2
}

View User Bookings

Endpoint: GET /bookings/


View Event Details

Endpoint: GET /events/{event_id}/

List and Filter Events

Endpoint: GET /events/

/events/?date=2023-12-25&location=1  






Register: POST /api/register/


{

   "email": "user@example.com",

   "name": "John Doe",

   "username": "johndoe",

   "password": "password123"

}



Logout: POST /api/logout/


Create Event (Event Manager Only): POST /api/create-event/


{

   "title": "Concert",

   "description": "Live music concert",

   "date": "2024-07-01",

   "time": "18:00",

   "location": "Stadium",

   "payment_options": "Credit Card, PayPal"

}







Book Ticket: POST /api/book-ticket/


{

   "event_id": 1,

   "number_of_tickets": 2

}



Filter Events: GET /api/events/?location=Stadium&date=2024-07-01&category=Music


Make Payment: POST /api/make-payment/


{

   "booking_id": 1,

   "payment_method": "Credit Card",

   "amount": 100

}



Revert Payment: POST /api/revert-payment/


{

   "booking_id": 1,

   "reason": "Booking canceled"

}
