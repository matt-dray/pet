import datetime
from pathlib import Path
from pet import utils


def test_write_and_read_stats(tmp_path: Path):
    """Ensure we can write and read pet data."""
    test_file = tmp_path / "pet.json"
    name = "Brian"

    utils.init_stats(test_file, name)
    data = utils.read_stats(test_file)

    assert data["NAME"] == name
    assert data["BORN"] == data["LAST"]
    assert data["AGE"] == 0
    assert data["HEALTH"] == 10


def test_get_datetime():
    """Ensure date and time are extracted correctly from saved timestamp."""
    now = datetime.datetime.now()
    iso_str = now.isoformat()

    birth_dt = utils.get_datetime(iso_str)

    assert isinstance(birth_dt, dict)
    assert isinstance(birth_dt["DATE"], str)
    assert isinstance(birth_dt["TIME"], str)
    assert str(now.year) in birth_dt["DATE"]


def test_delete_stats(tmp_path: Path):
    """Make sure pet data file gets deleted."""
    test_file = tmp_path / "pet.json"
    test_file.write_text("{'NAME': 'Brian'}")

    utils.delete_stats(test_file)

    assert not test_file.exists()
