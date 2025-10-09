from django.test import TestCase
from base.models import Task
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.task1 = Task.objects.create(
            user = self.user,
            title = "Wash Car",
            description = "Wash the car",
            complete = False,
        )

    def test_task_string_is_assigned(self):
        self.assertEqual(str(self.task1), 'Wash Car')

