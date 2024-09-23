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