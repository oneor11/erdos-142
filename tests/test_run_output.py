import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from erdos142.kap import kap_cache
from erdos142.reporting import RunOutput
from erdos142.search import r


class RunOutputTests(unittest.TestCase):
    def test_files_are_updated_after_each_completed_n(self):
        with tempfile.TemporaryDirectory(dir=Path.cwd()) as temporary_dir:
            with contextlib.redirect_stdout(io.StringIO()) as console:
                with RunOutput(3, temporary_dir) as output:
                    output.start(5, 4)
                    run_dir = output.run_dir
                    self.assertEqual(
                        (run_dir / "results_desmos.txt").read_text(encoding="utf-8"),
                        "[(5,4)]\n",
                    )

                    kap_cache.clear()
                    value, candidate, stats, cache_stats, depth_stats = r(6, 3, 4)
                    output.add_result(6, value, 4, candidate, stats, cache_stats, depth_stats)

                    # Files must already be complete while the run is still open.
                    self.assertEqual(
                        (run_dir / "results_compact.txt").read_text(encoding="utf-8"),
                        "N | r_3(N)\n5 | 4\n6 | 4\n",
                    )
                    self.assertEqual(
                        (run_dir / "results_desmos.txt").read_text(encoding="utf-8"),
                        "[(5,4), (6,4)]\n",
                    )
                    self.assertEqual(
                        (run_dir / "results_verbose.txt").read_text(encoding="utf-8"),
                        console.getvalue(),
                    )
                    self.assertIn("RESULT FOR N = 6", console.getvalue())

    def test_interruption_keeps_completed_results(self):
        with tempfile.TemporaryDirectory(dir=Path.cwd()) as temporary_dir:
            with contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(KeyboardInterrupt):
                    with RunOutput(4, temporary_dir) as output:
                        output.start(5, 4)
                        run_dir = output.run_dir
                        raise KeyboardInterrupt
            self.assertEqual(
                (run_dir / "results_desmos.txt").read_text(encoding="utf-8"),
                "[(5,4)]\n",
            )
            self.assertEqual(
                (run_dir / "results_compact.txt").read_text(encoding="utf-8"),
                "N | r_4(N)\n5 | 4\n",
            )


if __name__ == "__main__":
    unittest.main()
