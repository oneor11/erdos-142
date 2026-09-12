"""Console reports for search, cache, and depth statistics."""

import os

from erdos142.kap import kap_cache

try:
    import psutil
    process = psutil.Process(os.getpid())
    PSUTIL_AVAILABLE = True
except ImportError:
    process = None
    PSUTIL_AVAILABLE = False

def print_result(
    N,
    r_value,
    stats
):

    print()
    print(f"RESULT FOR N = {N}")
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