"""Backtracking search and its instrumentation."""

from collections import defaultdict
from time import perf_counter

from erdos142.kap import creates_kAP, value_bit

def make_depth_stats():
    return defaultdict(
        lambda: {
            "nodes": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "choices_tried": 0,
            "ap_prunes": 0,
            "lookahead_prunes": 0,
            "choices_survived": 0,
            "candidates_yielded": 0,
        }
    )



def generate_AP_free_candidates(
    S,
    size: int,
    k: int,
    stats: dict,
    cache_stats: dict,
    depth_stats,
    branch_ordering: str = "natural",
):
    """
    Generate AP-free subsets of S having exactly 'size'
    elements.

    Branches are pruned when:
      1. Adding x immediately creates a k-AP.
      2. Look-ahead shows that too few future values remain
         individually eligible to reach the target size.

    Natural ordering stops the look-ahead count once feasibility is known.
    Least-constrained ordering counts all eligible future values and visits
    surviving siblings from highest count to lowest (ties keep S order).
    """

    if branch_ordering not in ("natural", "least_constrained"):
        raise ValueError(f"Unknown branch ordering: {branch_ordering}")

    S = list(S)

    if not S:
        return

    min_value = S[0]

    def backtrack(
        start: int,
        current: list,
        current_mask: int
    ):

        depth = len(current)

        stats["nodes"] += 1
        depth_stats[depth]["nodes"] += 1

        # ----------------------------------------------------
        # TARGET SIZE REACHED
        # ----------------------------------------------------

        if depth == size:

            stats["candidates_yielded"] += 1
            depth_stats[depth]["candidates_yielded"] += 1

            yield tuple(current)
            return

        # ----------------------------------------------------
        # TRY EACH POSSIBLE NEXT VALUE
        # ----------------------------------------------------

        surviving_branches = [] if branch_ordering == "least_constrained" else None

        for i in range(start, len(S)):

            x = S[i]

            stats["choices_tried"] += 1
            depth_stats[depth]["choices_tried"] += 1

            # ------------------------------------------------
            # IMMEDIATE AP PRUNE
            # ------------------------------------------------

            if creates_kAP(
                current_mask,
                x,
                k,
                cache_stats,
                depth_stats,
                depth,
                min_value
            ):

                stats["ap_prunes"] += 1
                depth_stats[depth]["ap_prunes"] += 1

                continue

            # ------------------------------------------------
            # TEMPORARILY ADD x USING BITMASK
            # ------------------------------------------------

            test_mask = (
                current_mask
                | value_bit(x)
            )

            needed_after_x = (
                size - (depth + 1)
            )

            eligible_after_x = 0

            # ------------------------------------------------
            # LOOK-AHEAD PRUNING
            # ------------------------------------------------

            if needed_after_x > 0 or branch_ordering == "least_constrained":

                for j in range(
                    i + 1,
                    len(S)
                ):

                    y = S[j]

                    if not creates_kAP(
                        test_mask,
                        y,
                        k,
                        cache_stats,
                        depth_stats,
                        depth,
                        min_value
                    ):

                        eligible_after_x += 1

                        # We only need to know whether
                        # enough eligible values exist.
                        if (
                            branch_ordering == "natural"
                            and eligible_after_x >= needed_after_x
                        ):
                            break

            # ------------------------------------------------
            # NOT ENOUGH ELIGIBLE FUTURE VALUES
            # ------------------------------------------------

            if (
                eligible_after_x
                < needed_after_x
            ):

                stats["lookahead_prunes"] += 1
                depth_stats[depth]["lookahead_prunes"] += 1

                continue

            # ------------------------------------------------
            # BRANCH SURVIVES
            # ------------------------------------------------

            stats["choices_survived"] += 1
            depth_stats[depth]["choices_survived"] += 1

            if surviving_branches is not None:
                surviving_branches.append((x, i, test_mask, eligible_after_x))
                continue

            current.append(x)

            yield from backtrack(
                i + 1,
                current,
                test_mask
            )

            current.pop()

        if surviving_branches is not None:
            # Python's stable sort preserves original index order for ties.
            surviving_branches.sort(key=lambda branch: branch[3], reverse=True)
            for x, i, test_mask, eligible_after_x in surviving_branches:
                current.append(x)
                yield from backtrack(i + 1, current, test_mask)
                current.pop()

    yield from backtrack(
        0,
        [],
        0
    )



def r(
    N: int,
    k: int,
    previous_max: int,
    branch_ordering: str = "natural",
):
    """
    Given r_k(N-1) = previous_max, test whether r_k(N)
    increases by one.

    Since adding one new element to the universe can increase
    the maximum AP-free subset size by at most one:

        r_k(N) ∈ {previous_max, previous_max + 1}

    branch_ordering is "natural" or "least_constrained".
    """

    stats = {
        "branch_ordering": branch_ordering,
        "nodes": 0,
        "choices_tried": 0,
        "ap_prunes": 0,
        "lookahead_prunes": 0,
        "choices_survived": 0,
        "candidates_yielded": 0,
        "elapsed_seconds": 0.0,
    }

    cache_stats = {
        "hits": 0,
        "misses": 0,
        "true_hits": 0,
        "false_hits": 0,
        "true_stores": 0,
        "false_stores": 0,
    }

    depth_stats = make_depth_stats()

    target_size = previous_max + 1

    S = range(
        1,
        N + 1
    )

    start_time = perf_counter()

    # --------------------------------------------------------
    # STOP AT FIRST VALID TARGET-SIZE CANDIDATE
    # --------------------------------------------------------

    for candidate in generate_AP_free_candidates(
        S,
        target_size,
        k,
        stats,
        cache_stats,
        depth_stats,
        branch_ordering,
    ):

        stats["elapsed_seconds"] = (
            perf_counter()
            - start_time
        )

        return (
            target_size,
            candidate,
            stats,
            cache_stats,
            depth_stats
        )

    # --------------------------------------------------------
    # NO TARGET-SIZE CANDIDATE EXISTS
    # --------------------------------------------------------

    stats["elapsed_seconds"] = (
        perf_counter()
        - start_time
    )

    return (
        previous_max,
        None,
        stats,
        cache_stats,
        depth_stats
    )


