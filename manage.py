#!/usr/bin/env python
# This is the file in the main folder that runs the file as a
# reusable script

"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # sys.argv is a list in Python, which contains the command-line arguments passed to the script.
    execute_from_command_line(sys.argv)

# When putting this we indicate this is the main folder
# and run the code above for doing stuff through the sys

if __name__ == '__main__':
    main()
