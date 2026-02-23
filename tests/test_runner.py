import pytest

from pytest_bdd import scenarios
from tests.steps.test_worldMap_step import *
from tests.steps.test_drugProfile import *
from tests.steps.test_initialTask_step import *
from tests.steps.test_list_step import *
from tests.steps.test_overview_step import *
from tests.steps.test_dashboard_step import *

# Load both feature files
scenarios("features/list.feature")
scenarios("features/dashboard.feature")
scenarios("features/overview.feature")

@pytest.mark.order(1)
def test_task_list_feature():
    """Runs the Task List feature first."""
    pass

@pytest.mark.order(2)
def test_dashboard_feature():
    """Runs the Dashboard feature second."""
    pass

@pytest.mark.order(3)
def test_overview_feature():
    """Runs the Overview feature second."""
    pass

