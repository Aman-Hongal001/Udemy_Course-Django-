import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','level2_project.settings')

import django
django.setup()

from level2_app.models import *
from faker import Faker

fakergen = Faker()

def populate(N=5):
    for entry in range(N):
        #create the fake data for that entry
        fake_name = fakergen.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fakergen.email()
        
        # create the new webpage entry
        
        users= User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_email)[0]
        
        
if __name__ == '__main__':
    print("populating data!")
    populate(20)
    print("Populating complete")