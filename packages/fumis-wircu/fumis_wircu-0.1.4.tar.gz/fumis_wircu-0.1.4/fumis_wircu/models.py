"""Models for the Fumis WiRCU."""

from dataclasses import dataclass

from .const import STATE_MAPPING, STATE_UNKNOWN, STATUS_MAPPING, STATUS_UNKNOWN


@dataclass(frozen=True)
class Info:
    """Object holding information and states of the Fumis WiRCU device."""

    unit_id: str
    api_version: str

    unit_version: str
    unit_temperature: float
    controller_version: str

    ip: str
    rssi: int
    signal_strength: int

    state: str
    state_id: int
    status: str
    status_id: int

    temperature: float
    target_temperature: float

    heating_time: int
    igniter_starts: int
    misfires: int
    overheatings: int
    uptime: int

    @staticmethod
    def from_dict(data: dict):
        """Return device object from Fumis WiRCU device response."""
        controller = data.get("controller", {})
        unit = data.get("unit", {})

        stats = controller.get("statistic", {})
        temperatures = controller.get("temperatures", {})
        temperature = temperatures[0] if temperatures else {}

        rssi = int(unit.get("rssi", -100))
        signal_strength = rssi_to_signal_strength(rssi)

        status_id = controller.get("status", -1)
        status = STATUS_MAPPING.get(status_id, STATUS_UNKNOWN)

        state_id = controller.get("command", -1)
        state = STATE_MAPPING.get(state_id, STATE_UNKNOWN)

        return Info(
            api_version=data.get("apiVersion", "Unknown"),
            unit_temperature=unit.get("temperature", 0),
            controller_version=controller.get("version", "Unknown"),
            heating_time=int(stats.get("heatingTime", 0)),
            igniter_starts=stats.get("igniterStarts", 0),
            ip=unit.get("ip", "Unknown"),
            misfires=stats.get("misfires", 0),
            overheatings=stats.get("overheatings", 0),
            rssi=rssi,
            signal_strength=signal_strength,
            state_id=state_id,
            state=state,
            status_id=status_id,
            status=status,
            target_temperature=temperature.get("set", 0),
            temperature=temperature.get("actual", 0),
            unit_id=unit.get("id", "Unknown"),
            unit_version=unit.get("version", "Unknown"),
            uptime=int(stats.get("uptime", 0)),
        )


def rssi_to_signal_strength(rssi: int) -> int:
    """Convert rssi into signal strength."""
    if rssi <= -100:
        return 0
    if -100 < rssi <= -50:
        return 2 * (rssi + 100)
    return 100
