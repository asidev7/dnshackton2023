# myapp/management/commands/generate_codes.py
import secrets
import string
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from account.models import CodeRecharge, Balance

class Command(BaseCommand):
    help = 'Generate recharge codes and settle balances'
    

    def handle(self, *args, **options):
        # Generate codes and settle balances for each amount
        amounts = [500, 1000, 5000, 10000]
        for amount in amounts:
            self.generate_and_settle(amount)

    def generate_and_settle(self, amount):
        # Generate 100 codes and settle balances
        for _ in range(100):
            code = self.generate_code()
            self.create_code(code, amount)

    def generate_code(self):
        letters = string.ascii_letters
        digits = string.digits
        random_string = ''.join(secrets.choice(letters) for _ in range(8)) + ''.join(secrets.choice(digits) for _ in range(8))
        return random_string

    def create_code(self, code, amount):
        # Create CodeRecharge instance
        code_instance = CodeRecharge.objects.create(code_recharge=code)

        