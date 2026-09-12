"""Console reports for search, cache, and depth statistics."""

import os
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
from pathlib import Path

from erdos142.kap import kap_cache

try:
    import psutil
    process = psutil.Process(os.getpid())
    PSUTIL_AVAILABLE = True
except ImportError:
    process = None
    PSUTIL_AVAILABLE = False


class RunOutput:
    """Write one experiment's reports after each completed N."""

    def __init__(self, k, output_dir=None, branch_ordering="natural"):
        if output_dir is None:
            output_dir = Path(__file__).resolve().parents[2] / "output"
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
        for suffix in range(1000):
            name = f"run {stamp}" if suffix == 0 else f"run {stamp}_{suffix}"
            self.run_dir = output_dir / name
            try:
                self.run_dir.mkdir()
                break
            except FileExistsError:
                continue
        else:
            raise FileExistsError("Could not create a unique run directory")

        self.k = k
        self.branch_ordering = branch_ordering
        self.points = []
        self.compact = (self.run_dir / "results_compact.txt").open("w", encoding="utf-8")
        self.verbose = (self.run_dir / "results_verbose.txt").open("w", encoding="utf-8")
        self.desmos = (self.run_dir / "results_desmos.txt").open("w", encoding="utf-8")
        self._write(self.compact, f"N | r_{k}(N)\n")
        self._write(self.desmos, "[]\n")

    @staticmethod
    def _write(file, content):
        file.write(content)
        file.flush()
        os.fsync(file.fileno())

    def _add_point(self, n, value):
        self.points.append((n, value))
        self._write(self.compact, f"{n} | {value}\n")
        points = ", ".join(f"({x},{y})" for x, y in self.points)
        self.desmos.seek(0)
        self.desmos.truncate()
        self._write(self.desmos, f"[{points}]\n")

    def _show_and_save(self, content):
        print(content, end="")
        self._write(self.verbose, content)

    def start(self, n_start, max_size):
        self._show_and_save(
            f"N = {n_start}, r_{self.k}({n_start}) = {max_size}\n"
            f"Branch ordering: {self.branch_ordering}\n"
            + "=" * 130 + "\n"
        )
        self._add_point(n_start, max_size)

    def add_result(self, n, value, previous_max, candidate, stats, cache_stats, depth_stats):
        report = StringIO()
        with redirect_stdout(report):
            print_result(n, value, stats)
            print_cache_summary(cache_stats)
            print_depth_stats(n, previous_max + 1, depth_stats)
            if candidate is not None:
                print()
                print(f"Candidate: {candidate}")
            print()
            print("=" * 130)
        self._show_and_save(report.getvalue())
        self._add_point(n, value)

    def close(self):
        self.compact.close()
        self.verbose.close()
        self.desmos.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

def print_result(
    N,
    r_value,
    stats
):

    print()
    print(f"RESULT FOR N = {N}")
    print(f"Branch ordering: {stats.get('branch_ordering', 'natural')}")
    print()

    header = (
        f"{'N':>3} | "
        f"{'r_k(N)':>6} | "
        f"{'Seconds':>10} | "
        f"{'Nodes':>12} | "
        f"{'Tried':>12} | "
        f"{'AP Prunes':>12} | "
        f"{'LA Prunes':>12} | "
        f"{'Survived':>12} | "
        f"{'Yielded':>8}"
    )

    print(header)
    print("-" * len(header))

    print(
        f"{N:>3} | "
        f"{r_value:>6} | "
        f"{stats['elapsed_seconds']:>10.4f} | "
        f"{stats['nodes']:>12,} | "
        f"{stats['choices_tried']:>12,} | "
        f"{stats['ap_prunes']:>12,} | "
        f"{stats['lookahead_prunes']:>12,} | "
        f"{stats['choices_survived']:>12,} | "
        f"{stats['candidates_yielded']:>8,}"
    )


def print_cache_summary(
    cache_stats
):

    hits = cache_stats["hits"]
    misses = cache_stats["misses"]

    true_hits = cache_stats["true_hits"]
    false_hits = cache_stats["false_hits"]

    true_stores = cache_stats["true_stores"]
    false_stores = cache_stats["false_stores"]

    total_calls = (
        hits + misses
    )

    hit_rate = (
        hits / total_calls
        if total_calls
        else 0
    )

    true_reuse_rate = (
        true_hits / true_stores
        if true_stores
        else 0
    )

    false_reuse_rate = (
        false_hits / false_stores
        if false_stores
        else 0
    )

    print()

    print(f"Cache Hits:          {hits:,}")
    print(f"Cache Misses:        {misses:,}")
    print(f"Cache Hit Rate:      {hit_rate:.2%}")

    print()

    print(f"True Cache Hits:     {true_hits:,}")
    print(f"False Cache Hits:    {false_hits:,}")

    print()

    print(f"True Stores:         {true_stores:,}")
    print(f"False Stores:        {false_stores:,}")

    print()

    print(
        f"True Reuse Ratio:    "
        f"{true_reuse_rate:.3f}"
    )

    print(
        f"False Reuse Ratio:   "
        f"{false_reuse_rate:.3f}"
    )

    print()

    print(
        f"Cache Entries:       "
        f"{len(kap_cache):,}"
    )

    if PSUTIL_AVAILABLE:

        memory_gb = (
            process.memory_info().rss
            / (1024 ** 3)
        )

        print(
            f"Process Memory:      "
            f"{memory_gb:.3f} GB"
        )


def print_depth_stats(
    N,
    target_size,
    depth_stats
):

    if not depth_stats:
        return

    max_node_depth = max(
        depth_stats,
        key=lambda depth:
            depth_stats[depth]["nodes"]
    )

    max_nodes = (
        depth_stats[
            max_node_depth
        ]["nodes"]
    )

    print()

    print(
        f"Max node depth: "
        f"{max_node_depth} "
        f"({max_nodes:,} nodes)"
    )

    print()

    print(
        f"Depth statistics for N = {N}, "
        f"searching for subset size "
        f"{target_size}"
    )

    print()

    header = (
        f"{'Depth':>5} | "
        f"{'Nodes':>12} | "
        f"{'Cache Hits':>12} | "
        f"{'Cache Misses':>12} | "
        f"{'Tried':>12} | "
        f"{'AP Prunes':>12} | "
        f"{'LA Prunes':>12} | "
        f"{'Survived':>12} | "
        f"{'Yielded':>8}"
    )

    print(header)
    print("-" * len(header))

    for depth in sorted(
        depth_stats
    ):

        ds = depth_stats[depth]

        print(
            f"{depth:>5} | "
            f"{ds['nodes']:>12,} | "
            f"{ds['cache_hits']:>12,} | "
            f"{ds['cache_misses']:>12,} | "
            f"{ds['choices_tried']:>12,} | "
            f"{ds['ap_prunes']:>12,} | "
            f"{ds['lookahead_prunes']:>12,} | "
            f"{ds['choices_survived']:>12,} | "
            f"{ds['candidates_yielded']:>8,}"
        )
