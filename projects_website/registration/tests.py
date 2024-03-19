from django.test import TestCase
from django.contrib.auth.models import User
from registration.models import Customer, Lecturer, Student

class UserCreationTest(TestCase):
    def test_user_creation_student_group(self):
        user = User.objects.create(username='test_student', password='password')
        user.groups.create(name='student')
        self.assertIsNotNone(Student.objects.get(user=user))

    def test_user_creation_lecturer_group(self):
        user = User.objects.create(username='test_lecturer', password='password')
        user.groups.create(name='lecturer')
        self.assertIsNotNone(Lecturer.objects.get(user=user))

    def test_user_creation_customer_group(self):
        user = User.objects.create(username='test_customer', password='password')
        user.groups.create(name='customer')
        self.assertIsNotNone(Customer.objects.get(user=user))