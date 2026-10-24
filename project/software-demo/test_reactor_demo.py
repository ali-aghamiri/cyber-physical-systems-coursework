"""Behavioral checks for logical-time ordering and bounded execution."""

import unittest

from reactor_demo import LogicalScheduler, Tag, simulate


class ReactorDemoTests(unittest.TestCase):
    def test_same_time_events_follow_causal_microsteps(self) -> None:
        trace = simulate([(0, 25.0), (0, 32.0)])
        self.assertEqual([tag for tag, _, _ in trace],
                         [Tag(0, 0), Tag(0, 0), Tag(0, 1), Tag(0, 1), Tag(0, 2), Tag(0, 2)])
        self.assertEqual([name for _, name, _ in trace],
                         ["sensor", "sensor", "controller", "controller", "actuator", "actuator"])
        self.assertEqual([value for _, name, value in trace if name == "actuator"], [0.0, 1.0])
        self.assertEqual(trace, simulate([(0, 25.0), (0, 32.0)]))

    def test_future_event_and_past_rejection(self) -> None:
        scheduler = LogicalScheduler()
        seen = []

        def handler(value: float) -> None:
            seen.append(scheduler.current_tag)
            if value == 1:
                scheduler.schedule("self", 2, 5)
            else:
                with self.assertRaises(ValueError):
                    scheduler.schedule("self", 3, 4)

        scheduler.register("self", handler)
        scheduler.schedule("self", 1, 0)
        self.assertEqual(scheduler.run(), 2)
        self.assertEqual(seen, [Tag(0, 0), Tag(5, 0)])

    def test_zero_delay_cycle_is_bounded(self) -> None:
        scheduler = LogicalScheduler()
        scheduler.register("cycle", lambda value: scheduler.schedule("cycle", value, 0))
        scheduler.schedule("cycle", 1, 0)
        with self.assertRaisesRegex(RuntimeError, "event limit"):
            scheduler.run(max_events=10)


if __name__ == "__main__":
    unittest.main()

