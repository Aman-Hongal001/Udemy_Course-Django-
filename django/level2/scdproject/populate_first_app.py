import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','scdproject.settings')

import django
django.setup()

import random
from first_app.models import *
from faker import Faker

fakergen = Faker()
topic = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()
        #create the fake data for that entry
        fake_url = fakergen.url()
        fake_date = fakergen.date()
        fake_name = fakergen.company()
        
        # create the new webpage entry
        
        webp = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        
        acc_rec = AccessRecord.objects.get_or_create(name=webp,date=fake_date)[0]
        
if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("Populating complete")