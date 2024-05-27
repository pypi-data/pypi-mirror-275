import os
import sys

def main():
    # Add the backend directory to the Python path
    current_path = os.path.dirname(os.path.abspath(__file__))
    backend_path = os.path.join(current_path, 'backend')
    sys.path.append(backend_path)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
