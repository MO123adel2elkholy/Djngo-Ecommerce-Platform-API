import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import CommandError
import pathlib


@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user
    """
    return django_user_model.objects.create_superuser(
        "admin", "a@a.com", "admin"
    )


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixtures or create admin if fixture missing
    """
    User = get_user_model()
    with django_db_blocker.unblock():
        try:
            # try by fixture name first (Django app fixture dirs / FIXTURE_DIRS)
            call_command("loaddata", "db_admin_fixture.json")
            call_command("loaddata", "db_category_fixture.json")
            call_command("loaddata", "db_product_fixture.json")
            
            print("it Worked first ")
        except CommandError:
            # try loading by absolute path relative to this file
            repo_root = pathlib.Path(__file__).resolve().parents[2]  # src/..
            fixture_path = repo_root / "src" / "ecommerce" / "dashboard" / "fixtures" / "db_admin_fixture.json"

            if fixture_path.exists():
                call_command("loaddata", str(fixture_path))
                print("it Worked second ")

            else:
                # fallback: create admin user programmatically
                if not User.objects.filter(username="admin").exists():
                    User.objects.create_superuser("admin", "a@a.com", "admin")
                    print("it dosnt work at all ")
    yield