from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Student


@receiver(post_save, sender=Student)
def student_created(sender, instance, created, **kwargs):

    if created:
        print("--------------------------------")
        print("NEW STUDENT REGISTERED!")
        print("Student Name:", instance.name)
        print("Student Email:", instance.email)
        print("--------------------------------")