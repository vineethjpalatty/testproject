from django.core.management.base import BaseCommand

# import UserFactory here
import factory
import factory.django

from useraccount.models import UserDetail, ActivityPeriod

# factory.Faker._DEFAULT_LOCALE = 'en_US'
#
#
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDetail

    user_id = factory.Faker('user_id')
    username = factory.Faker('username')
    timezone = factory.Faker('timezone')


# class ActivityPeriodFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = ActivityPeriod
#
#     user = factory.Faker('user')
#     start_time = factory.Faker('start_time')
#     end_time = factory.Faker('end_time')


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=3,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for _ in range(options['users']):
            UserFactory.create()