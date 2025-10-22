import datetime as dt
from pathlib import Path
from pet import utils


def test_write_and_read_pet_data(tmp_path: Path):
    """Ensure we can write and read pet data."""
    test_file = tmp_path / "pet.json"
    timestamp = dt.datetime(2024, 1, 1, 12, 0, 0)
    name = "Brian"

    utils.write_pet_data(test_file, name, timestamp)
    data = utils.read_pet_data(test_file)

    assert data["NAME"] == name
    assert data["TIMESTAMP"] == timestamp.isoformat()


def test_extract_timestamp_and_delta():
    """Ensure timestamp handling works."""
    now = dt.datetime.now()
    iso_str = now.isoformat()

    # Check readable timestamp format
    readable = utils.extract_timestamp(iso_str)
    assert isinstance(readable, str)
    assert str(now.year) in readable

    # Check delta returns an int and near-zero for 'now'
    delta = utils.calculate_time_delta(iso_str)
    assert isinstance(delta, int)
    assert delta >= 0


def test_pet_data_gets_deleted(tmp_path: Path):
    """Make sure pet data file gets deleted."""
    test_file = tmp_path / "pet.json"
    test_file.write_text("{'NAME': 'Brian'}")

    utils.delete_pet_data(test_file)

    assert not test_file.exists()
