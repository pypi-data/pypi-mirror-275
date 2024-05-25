import pytest
import sqlalchemy as sa
import unittest.mock

import falcon.testing
import falcon_helpers.app as app
import falcon_helpers.sqla.db as db

bind = sa.engine.create_engine('sqlite://')
Base = sa.orm.declarative_base()

db.session.configure(bind=bind)


@pytest.fixture()
def api():
    return app.App()


@pytest.fixture()
def client(api):
    return falcon.testing.TestClient(api)


@pytest.fixture()
def mocked_sentry_client():
    with unittest.mock.patch(
        'falcon_helpers.plugins.sentry.raven.Client',
        spec_set=True,
        autospec=True
    ) as m:

        yield m
