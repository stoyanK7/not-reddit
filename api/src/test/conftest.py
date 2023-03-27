"""This module is used to store pytest fixtures."""

import pytest
from .database import session


@pytest.fixture
def remove_json_fields():
    """Remove a field from a JSON object."""

    def _remove_json_fields(json_object, *field_names):
        for field_name in field_names:
            json_object.pop(field_name, None)
        return json_object

    yield _remove_json_fields
