"""Tests for rssi to signal strength formula."""

from fumis_wircu.models import rssi_to_signal_strength


def test_rssi_to_signal_strength():
    """Test converting rssi to signal strength."""
    assert rssi_to_signal_strength(-300) == 0
    assert rssi_to_signal_strength(-60) == 80
    assert rssi_to_signal_strength(-30) == 100
