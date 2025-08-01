import pytest
import requests
from tenacity import stop_after_attempt

from truss.local.local_config_handler import LocalConfigHandler
from truss.tests.test_testing_utilities_for_other_tests import ensure_kill_all
from truss.truss_handle.truss_handle import TrussHandle


@pytest.mark.integration
@pytest.mark.parametrize(
    "test_truss", ["test_custom_server_truss", "test_go_custom_server_truss"]
)
def test_custom_server_truss(test_data_path, test_truss):
    with ensure_kill_all():
        print("Running test_custom_server_truss")
        truss_dir = test_data_path / test_truss
        print(f"truss_dir: {truss_dir}")
        tr = TrussHandle(truss_dir)
        print("Setting secret")
        LocalConfigHandler.set_secret("hf_access_token", "123")
        try:
            print("Starting container")
            _, urls = tr.docker_run_for_test(
                model_server_stop_retry_override=stop_after_attempt(10)
            )
        except Exception as e:
            raise Exception(f"Failed to start container: {e}")

        response = requests.post(urls.predict_url, json={})
        assert response.status_code == 200
        assert response.json() == {
            "message": "Hello World",
            "is_env_var_passed": True,
            "is_secret_mounted": True,
        }
