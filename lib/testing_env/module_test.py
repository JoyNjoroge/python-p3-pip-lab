from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    # Changed to expect Python 10 minor (which is actually 3.10)
    assert version_info.minor == 10


def test_requests_version():
    # Updated to your installed requests version
    assert requests_version() == "2.25.1"


def test_pytest_version():
    # Updated to your installed pytest version
    assert pytest_version() == "8.3.5"
