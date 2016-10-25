import json
import unittest
import data_kobe_util

class TestSync(unittest.TestCase):
	def test_sync(self):
		diff = data_kobe_util.diff()
		assert not diff, json.dumps(diff, indent=2, ensure_ascii=False)

