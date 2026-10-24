"""A small, deterministic logical-time scheduler inspired by reactor programs.

This is a software teaching example, not a Lingua Franca runtime or a Zephyr
benchmark. It models event ordering only; wall-clock timing is not measured.
"""

from __future__ import annotations

import argparse
import heapq
from dataclasses import dataclass, field
from typing import Callable


@dataclass(frozen=True, order=True)
class Tag:
    time_ms: int
    microstep: int = 0


@dataclass(order=True)
class Event:
    tag: Tag
    sequence: int
    target: str = field(compare=False)
    value: float = field(compare=False)


class LogicalScheduler:
    """Deliver events in (logical time, microstep, insertion order)."""

    def __init__(self) -> None:
        self._queue: list[Event] = []
        self._handlers: dict[str, Callable[[float], None]] = {}
        self._sequence = 0
        self.current_tag: Tag | None = None

    def register(self, name: str, handler: Callable[[float], None]) -> None:
        if name in self._handlers:
            raise ValueError(f"duplicate reactor: {name}")
        self._handlers[name] = handler

    def schedule(self, target: str, value: float, time_ms: int) -> None:
        if target not in self._handlers:
            raise ValueError(f"unknown reactor: {target}")
        if time_ms < 0 or (self.current_tag and time_ms < self.current_tag.time_ms):
            raise ValueError("cannot schedule an event in the past")
        microstep = 0
        if self.current_tag and time_ms == self.current_tag.time_ms:
            microstep = self.current_tag.microstep + 1
        heapq.heappush(self._queue, Event(Tag(time_ms, microstep), self._sequence,
                                          target, value))
        self._sequence += 1

    def run(self, max_events: int = 10_000) -> int:
        if max_events < 1:
            raise ValueError("max_events must be positive")
        processed = 0
        while self._queue:
            if processed >= max_events:
                raise RuntimeError("event limit reached; possible zero-delay feedback loop")
            event = heapq.heappop(self._queue)
            self.current_tag = event.tag
            self._handlers[event.target](event.value)
            processed += 1
        return processed


def simulate(readings: list[tuple[int, float]], threshold: float = 30.0) -> list[tuple[Tag, str, float]]:
    """Route sensor readings through controller and actuator at logical tags.

    An actuator value of 1 means 'on' and 0 means 'off'. Same-time reactions
    advance by one microstep, so each stage has a deterministic order.
    """
    scheduler = LogicalScheduler()
    trace: list[tuple[Tag, str, float]] = []

    def sensor(value: float) -> None:
        assert scheduler.current_tag is not None
        trace.append((scheduler.current_tag, "sensor", value))
        scheduler.schedule("controller", value, scheduler.current_tag.time_ms)

    def controller(value: float) -> None:
        assert scheduler.current_tag is not None
        command = float(value >= threshold)
        trace.append((scheduler.current_tag, "controller", command))
        scheduler.schedule("actuator", command, scheduler.current_tag.time_ms)

    def actuator(value: float) -> None:
        assert scheduler.current_tag is not None
        trace.append((scheduler.current_tag, "actuator", value))

    scheduler.register("sensor", sensor)
    scheduler.register("controller", controller)
    scheduler.register("actuator", actuator)
    for time_ms, value in readings:
        scheduler.schedule("sensor", value, time_ms)
    scheduler.run()
    return trace


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--threshold", type=float, default=30.0)
    args = parser.parse_args()
    for tag, reactor, value in simulate([(0, 25.0), (10, 32.0), (20, 28.0)], args.threshold):
        print(f"{tag.time_ms:>3} ms / microstep {tag.microstep}: {reactor:<10} {value:g}")


if __name__ == "__main__":
    main()

