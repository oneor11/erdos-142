import unittest

from erdos142.kap import creates_kAP, kap_cache, value_bit
from erdos142.search import make_depth_stats, r


class BitmaskTests(unittest.TestCase):
    def setUp(self):
        kap_cache.clear()

    def test_value_bit(self):
        self.assertEqual([value_bit(x) for x in range(1, 5)], [1, 2, 4, 8])

    def test_ap_completion_and_cache_instrumentation(self):
        cache_stats = dict.fromkeys(
            ("hits", "misses", "true_hits", "false_hits", "true_stores", "false_stores"), 0
        )
        depth_stats = make_depth_stats()
        mask = value_bit(1) | value_bit(3)

        self.assertTrue(creates_kAP(mask, 5, 3, cache_stats, depth_stats, 2))
        self.assertFalse(creates_kAP(mask, 4, 3, cache_stats, depth_stats, 2))
        self.assertTrue(creates_kAP(mask, 5, 3, cache_stats, depth_stats, 2))
        self.assertFalse(creates_kAP(mask, 4, 3, cache_stats, depth_stats, 2))
        self.assertEqual(cache_stats, {
            "hits": 2, "misses": 2, "true_hits": 1, "false_hits": 1,
            "true_stores": 1, "false_stores": 1,
        })
        self.assertEqual(depth_stats[2]["cache_hits"], 2)
        self.assertEqual(depth_stats[2]["cache_misses"], 2)


class SearchTests(unittest.TestCase):
    def setUp(self):
        kap_cache.clear()

    def test_small_known_r3_values(self):
        # The runner starts from the known exact value r_3(5) = 4.
        expected = {6: 4, 7: 4, 8: 4, 9: 5, 10: 5}
        maximum = 4
        for n, known_value in expected.items():
            kap_cache.clear()
            maximum, candidate, stats, cache_stats, depth_stats = r(n, 3, maximum)
            self.assertEqual(maximum, known_value, f"N={n}")
            self.assertEqual(candidate is not None, known_value > expected.get(n - 1, 4))
            self.assertEqual(stats["nodes"], sum(row["nodes"] for row in depth_stats.values()))
            self.assertEqual(cache_stats["misses"],
                             cache_stats["true_stores"] + cache_stats["false_stores"])


if __name__ == "__main__":
    unittest.main()
