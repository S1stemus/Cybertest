import csv
from django.core.management.base import BaseCommand
from models.models import *

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    

    def handle(self, *args, **kwargs):
        csv_file_path = './data.csv'
        user = User.objects.get(id=1)
        if user is None:
            user = User.objects.create_user(username='admin', password='admin')

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    test=Test.objects.create(
                    name=row['test'],                        
                    )
                    test.user.set([user])
                    Question.objects.create(
                        name=row['question'],
                        test=Test.objects.filter(name=row['test']).first(),
                        user=user
                    )
                    Answer.objects.create(
                        name=row['true_answer'],
                        question=Question.objects.filter(name=row['question']).first(),
                        is_correct=1,
                        user=user,
                        choices=int(row['choices_true'])
                    )
                    Answer.objects.create(
                        name=row['false_answer'],
                        question=Question.objects.filter(name=row['question']).first(),
                        is_correct=0,
                        user=user,
                        choices=int(row['choices_false'])
                    )

            self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing data: {e}'))