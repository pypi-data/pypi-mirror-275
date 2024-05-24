from os import path
import unittest

from src.auto_switch_providers.auto_switch_providers import AutoSwitchProviders

TEMPLATE_CONFIG = {"googleapi": {"http_service": {"params": {"key": ""}}}}


class TestSample(unittest.TestCase):
    def test_process(self):
        response = AutoSwitchProviders(
            template_dir=f"{path.dirname(__file__)}/templates",
            config=TEMPLATE_CONFIG,
        ).process({})
        self.assertIn("data", response)


if __name__ == "__main__":
    unittest.main()
