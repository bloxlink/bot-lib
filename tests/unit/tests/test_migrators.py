import pytest
import mock
from bloxlink_lib.models.guilds import RestrictionTypes
from bloxlink_lib.validators import *


class TestRestrictionMigrator:
    """Tests related to migrating V3 restrictions to V4."""

    @pytest.fixture
    def model(self):
        return
