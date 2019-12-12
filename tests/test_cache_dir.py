import pip_api


def test_version():
    result = pip_api.cache_dir()

    assert "pip" in result
    assert "ache" in result
