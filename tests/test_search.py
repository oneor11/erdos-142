import unittest

from erdos142.kap import creates_kAP, kap_cache, value_bit
from erdos142.search import generate_AP_free_candidates, make_depth_stats, r


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

    def test_least_constrained_matches_small_known_values(self):
        expected = {6: 4, 7: 4, 8: 4, 9: 5, 10: 5, 11: 6, 12: 6}
        for mode in ("natural", "least_constrained"):
            maximum = 4
            for n, known_value in expected.items():
                kap_cache.clear()
                maximum, candidate, stats, _, depth_stats = r(n, 3, maximum, mode)
                self.assertEqual(maximum, known_value, (mode, n))
                self.assertEqual(stats["branch_ordering"], mode)
                self.assertEqual(stats["nodes"], sum(row["nodes"] for row in depth_stats.values()))
                if candidate is not None:
                    self.assertEqual(len(candidate), maximum)
                    self.assertTrue(self._is_ap_free(candidate))

    @staticmethod
    def _is_ap_free(candidate):
        values = set(candidate)
        return all(not (a + d in values and a + 2 * d in values)
                   for a in candidate for d in range(1, max(candidate) + 1))

    def test_no_witness_explores_same_branches(self):
        runs = []
        for mode in ("natural", "least_constrained"):
            kap_cache.clear()
            value, candidate, stats, _, _ = r(8, 3, 4, mode)
            self.assertEqual((value, candidate), (4, None))
            runs.append(stats)
        for key in ("nodes", "choices_tried", "ap_prunes", "lookahead_prunes",
                    "choices_survived", "candidates_yielded"):
            self.assertEqual(runs[0][key], runs[1][key], key)
        self.assertEqual(runs[0]["nodes"], 18)

    def test_full_scores_change_witness_order(self):
        def first_candidate(mode):
            kap_cache.clear()
            stats = dict.fromkeys(("nodes", "choices_tried", "ap_prunes",
                                   "lookahead_prunes", "choices_survived", "candidates_yielded"), 0)
            cache_stats = dict.fromkeys(("hits", "misses", "true_hits", "false_hits",
                                         "true_stores", "false_stores"), 0)
            return next(generate_AP_free_candidates(
                range(1, 8), 3, 3, stats, cache_stats, make_depth_stats(), mode
            ))

        self.assertEqual(first_candidate("natural"), (1, 2, 4))
        self.assertEqual(first_candidate("least_constrained"), (1, 2, 5))

    def test_unknown_branch_ordering_is_rejected(self):
        with self.assertRaises(ValueError):
            r(6, 3, 4, "unknown")


if __name__ == "__main__":
    unittest.main()
