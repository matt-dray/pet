import datetime as dt
from pathlib import Path
from pet import utils


def test_write_and_read_stats(tmp_path: Path):
    """Ensure we can write and read pet data."""
    test_file = tmp_path / "pet.json"
    timestamp = dt.datetime(2025, 10, 22, 22, 51, 0)
    name = "Brian"
    hp = 10

    utils.write_stats(test_file, name, timestamp)
    data = utils.read_stats(test_file)

    assert data["NAME"] == name
    assert data["TIMESTAMP"] == timestamp.isoformat()
    assert data["HP"] == hp


def test_get_birth_datetime():
    """Ensure date and time are extracted correctly from saved timestamp."""
    now = dt.datetime.now()
    iso_str = now.isoformat()

    birth_dt = utils.get_birth_datetime(iso_str)

    assert isinstance(birth_dt, dict)
    assert isinstance(birth_dt["DATE"], str)
    assert isinstance(birth_dt["TIME"], str)
    assert str(now.year) in birth_dt["DATE"]


def test_get_birth_delta():
    """Ensure delta is calculated correctly from saved timestamp to now."""
    now = dt.datetime.now()
    iso_str = now.isoformat()

    birth_delta = utils.get_birth_delta(iso_str)

    assert isinstance(birth_delta, dict)
    assert isinstance(birth_delta["HOURS"], int)
    assert isinstance(birth_delta["MINS"], int)


def test_delete_stats(tmp_path: Path):
    """Make sure pet data file gets deleted."""
    test_file = tmp_path / "pet.json"
    test_file.write_text("{'NAME': 'Brian'}")

    utils.delete_stats(test_file)

    assert not test_file.exists()
