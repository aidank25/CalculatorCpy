import pytest
from app.env_vars import EnvVars

def test_app_get_environment_variable():
    environment_vars = EnvVars()
#   Retrieve the current environment variables
    test1 = environment_vars.get_environment_variable('TEST1')
    test2 = environment_vars.get_environment_variable('TEST2')
    # Assert that the current environment is what you expect
    assert test1 == 'secret1', f"Invalid TEST: {test1}"
    assert test2 == 'secret2', f"Invalid TEST: {test2}"

