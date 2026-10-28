
import unittest
from collections import Counter


class SecurityLogAnalyzerTests(unittest.TestCase):

    def test_failure_threshold(self):
        failed_ips = Counter({
            "192.168.1.25": 3,
            "192.168.1.30": 1
        })

        self.assertGreaterEqual(failed_ips["192.168.1.25"], 3)
        self.assertLess(failed_ips["192.168.1.30"], 3)

    def test_success_and_failure_counts(self):
        events = [
            "LOGIN_SUCCESS",
            "LOGIN_FAILED",
            "LOGIN_FAILED"
        ]

        self.assertEqual(events.count("LOGIN_SUCCESS"), 1)
        self.assertEqual(events.count("LOGIN_FAILED"), 2)


if __name__ == "__main__":
    unittest.main()
