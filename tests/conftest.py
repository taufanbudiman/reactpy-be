import os

import pytest
from flask_jwt_extended import create_access_token

from app import create_app
from app.tasks.models import Tasks
from app.extensions import db

basedir = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture(autouse=True, scope="session")
def app_dict():
    os.environ["DEVELOPMENT_DATABASE_URL"] = 'db_test.db'
    app = create_app()

    # other setup can go here

    with app.app_context():
        db.create_all()

        yield {"app": app, "db": db}

        db.session.remove()
        if "test" in app.config["SQLALCHEMY_DATABASE_URI"]:
            db.drop_all()

    # clean up / reset resources here


@pytest.fixture(autouse=True, scope="session")
def authentication_header():
    access_token = create_access_token('testuser')
    return {"authorization": "Bearer {}".format(access_token)}


@pytest.fixture()
def client(app_dict, authentication_header):
    """
    Smaller initialization and teardown for each individual unit test.
    """
    app = app_dict["app"]
    base_db = app_dict["db"]
    client = app.test_client()

    yield client

    clean_db_contents(
        db_to_clean=base_db,
        # Tables are cleared in order of foreign key dependency.
        list_of_tables_to_clear=[
            Tasks,
        ],
    )
    base_db.session.rollback()


def clean_db_contents(db_to_clean, list_of_tables_to_clear: list):
    """
    Wipes all rows from database tables, for use at the end of unit tests.
    """
    for table in list_of_tables_to_clear:
        db_to_clean.session.query(table).delete()

    db_to_clean.session.commit()
