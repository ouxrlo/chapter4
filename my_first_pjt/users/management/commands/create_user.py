from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a user from the command line'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']

        # 사용자 모델 가져오기
        User = get_user_model()

        # 사용자 생성
        user = User.objects.create_user(username=username, password=password)
        self.stdout.write(self.style.SUCCESS(f"User {user.username} created successfully"))
