import datetime

from django.test import TestCase
from django.core.management import call_command
from downtime.models import Period
from .models import Banner


class BannerTest(TestCase):
    def test_is_active(self):
        """
        Tests the banner will be visible when the date range is applicable
        """
        self.p1 = Period.objects.create(
            id=123,
            enabled=True,
            start_time=datetime.datetime.now(),
            end_time=datetime.datetime.now() + datetime.timedelta(days=2)
        )
        self.b1 = Banner.objects.create(
            id=1234,
            message="Test banner",
            period=self.p1,
            days=0
        )

        self.active_banner = Banner.objects.get_deployed().first()

        # The first active banner should be b1
        self.assertEqual(self.active_banner, self.b1)

        self.assertEqual(self.active_banner.period, self.p1)

        # Banner should be active initally
        self.assertTrue(self.active_banner, "Banner should be active")

        # Banner should be disabled if its period is disabled
        self.p1.enabled=False
        self.p1.save()
        self.active_banner = Banner.objects.get_deployed().first()
        self.assertFalse(self.active_banner, "Banner should not be active if its period is not enabled.")

        # Banner should be active if its period is enabled.
        self.p1.enabled=True
        self.p1.save()
        self.active_banner = Banner.objects.get_deployed().first()
        self.assertTrue(self.active_banner, "Banner should be active if its period is enabled.")

        # Change Period start_time to tomorrow
        self.p1.start_time = datetime.datetime.now() + datetime.timedelta(days=1)
        self.p1.save()

        # Banner should not be active, so active_banner will be empty
        self.active_banner = Banner.objects.get_deployed().first()
        self.assertFalse(self.active_banner, "Banner should not be active")

        # Change Banner day range to 1 day out
        self.b1.days=1
        self.b1.save()

        # Banner should be active
        self.active_banner=Banner.objects.get_deployed().first()
        self.assertTrue(self.active_banner, "Banner should be active")

        # Change Period start_time and end_time to some time in the past
        self.p1.start_time=datetime.datetime.now() - datetime.timedelta(days=9)
        self.p1.end_time=datetime.datetime.now() - datetime.timedelta(days=8)
        self.p1.save()

        # Banner should not be active, so active_banner will be empty
        self.active_banner = Banner.objects.get_deployed().first()
        self.assertFalse(self.active_banner, "Banner should not be active")

        # Set banner to disabled
        self.b1.disabled = True
        self.b1.save()

        # Banner should not be active, so active_banner will be empty
        self.active_banner = Banner.objects.get_deployed().first()
        self.assertFalse(self.active_banner, "Banner should not be active if set to disabled.")


class CommandTest(TestCase):
    def test_disable_downtime(self):
        """
        Test disable_downtime management command.
        """
        self.p1 = Period.objects.create(
            id=123,
            enabled=True,
            start_time=datetime.datetime.now(),
            end_time=datetime.datetime.now() + datetime.timedelta(days=2)
        )

        self.p2 = Period.objects.create(
            id=124,
            enabled=False,
            start_time=datetime.datetime.now(),
            end_time=datetime.datetime.now() + datetime.timedelta(days=2)
        )

        self.active_periods = Period.objects.active()

        self.assertTrue(self.active_periods, "Period 1 should be active initally.")

        # Call disable_downtime command
        call_command('disable_downtime')

        self.active_periods = Period.objects.active()
        self.assertFalse(self.active_periods, "Periods should all be disabled.")
