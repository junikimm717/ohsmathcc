from django.test import TestCase
from . import utils

# Create your tests here.

class ScheduleTimeTest(TestCase):

    def setUp(self):
        pass
    
    def test_1(self):
        schedule = iter(utils.ScheduleTime(6, 0))
        self.assertEqual(
            next(schedule), 
            f"06:00AM {utils.ScheduleTime.TIMEZONE}-07:15AM {utils.ScheduleTime.TIMEZONE}"
        )

    def test_2(self):
        schedule = iter(utils.ScheduleTime(10, 15))
        next(schedule)
        self.assertEqual(
            next(schedule), 
            f"11:30AM {utils.ScheduleTime.TIMEZONE}-12:45PM {utils.ScheduleTime.TIMEZONE}"
        )

    def test_3(self):
        schedule = iter(utils.ScheduleTime(22, 15))
        next(schedule)
        self.assertEqual(
            next(schedule), 
            f"11:30PM {utils.ScheduleTime.TIMEZONE}-12:45AM {utils.ScheduleTime.TIMEZONE}"
        )