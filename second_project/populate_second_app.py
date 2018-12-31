import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')


import django
django.setup()


from faker import Faker
import random
from second_app.models import User

fakegen = Faker()

def populate(N=10):
    for i in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_mail = fakegen.email()

        fake_user = User.objects.get_or_create(first_name=fake_first_name,
                                                last_name=fake_last_name,
                                                email=fake_mail)

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Complete!")