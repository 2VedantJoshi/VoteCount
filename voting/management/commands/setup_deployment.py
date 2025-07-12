from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Set up deployment by collecting static files and running migrations'

    def handle(self, *args, **options):
        self.stdout.write('Setting up deployment...')
        
        # Create staticfiles directory if it doesn't exist
        static_root = os.path.join(os.getcwd(), 'staticfiles')
        if not os.path.exists(static_root):
            os.makedirs(static_root)
            self.stdout.write('Created staticfiles directory')
        
        # Collect static files
        self.stdout.write('Collecting static files...')
        call_command('collectstatic', '--noinput')
        
        # Run migrations
        self.stdout.write('Running migrations...')
        call_command('migrate')
        
        self.stdout.write(self.style.SUCCESS('Deployment setup completed!')) 