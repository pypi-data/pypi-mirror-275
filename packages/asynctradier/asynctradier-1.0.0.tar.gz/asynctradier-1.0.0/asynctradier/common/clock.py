import strenum


class ClockState(strenum.StrEnum):
    PREMARKET = "premarket"
    OPEN = "open"
    POSTMARKET = "postmarket"
    CLOSED = "closed"


class Clock:
    def __init__(self, **kwargs):
        self.date = kwargs.get("date")
        self.description = kwargs.get("description")
        self.state = ClockState(kwargs.get("state")) if kwargs.get("state") else None
        self.timestamp = kwargs.get("timestamp")
        self.next_change = kwargs.get("next_change")
        self.next_state = (
            ClockState(kwargs.get("next_state")) if kwargs.get("next_state") else None
        )

    def __str__(self) -> str:
        return (
            f"Clock(date={self.date}, description={self.description}, "
            f"state={self.state}, timestamp={self.timestamp}, "
            f"next_change={self.next_change}, next_state={self.next_state})"
        )
