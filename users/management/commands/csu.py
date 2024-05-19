from django.core.management import BaseCommand
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from users.models import User


class Command(BaseCommand):
    help = 'Создание пользователя'

    def handle(self, *args, **options):
        email = input('Email: ').strip()
        try:
            validate_email(email)
        except ValidationError:
            self.stdout.write(self.style.ERROR('Некорректный email адрес'))
            return

        first_name = input('First name: ').strip()
        last_name = input('Last name: ').strip()
        phone = input('Phone: ').strip()

        positions = dict(User.POSITION)
        print("Выберите позицию:")
        for key, value in positions.items():
            print(f"{key}: {value}")

        position_key = input("Введите позицию сотрудника (admin/manager): ").strip()

        while position_key not in positions:
            print("Некорректная позиция. Пожалуйста, введите admin или manager.")
            position_key = input("Введите позицию сотрудника (admin/manager): ").strip()

        is_superuser = input('Сделать этого пользователя суперпользователем? (yes/no): ').strip().lower() == 'yes'

        password = input('Password: ').strip()

        if not User.objects.filter(email=email).exists():
            user = User.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                position=position_key,
                is_superuser=is_superuser,
                is_staff=True,
                phone=phone,
                is_active=True
            )
            user.set_password(password)
            user.save()
            user_type = "superuser" if is_superuser else "staff user"
            self.stdout.write(self.style.SUCCESS(f'{user_type}: {email} успешно создан'))
        else:
            self.stdout.write(self.style.WARNING(f'Сотрудник с таким email ({email}) уже существует'))
