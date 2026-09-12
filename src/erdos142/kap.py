"""Bitmask helpers and cached arithmetic-progression checks."""

kap_cache = {}

_NOT_CACHED = object()



def value_bit(x: int) -> int:
    """
    Convert integer x to its bit position.

    Example:
        1 -> 0001
        2 -> 0010
        3 -> 0100
        4 -> 1000
    """
    return 1 << (x - 1)



def creates_kAP(
    current_mask: int,
    x: int,
    k: int,
    cache_stats: dict,
    depth_stats,
    depth: int,
    min_value: int = 1
) -> bool:
    """
    Determine whether adding x to the current set creates
    a k-term arithmetic progression.

    Because values are added in increasing order, x must be
    the largest/final value of any newly created progression.
    """

    key = (current_mask, x)

    cached_result = kap_cache.get(
        key,
        _NOT_CACHED
    )

    # --------------------------------------------------------
    # CACHE HIT
    # --------------------------------------------------------

    if cached_result is not _NOT_CACHED:

        cache_stats["hits"] += 1
        depth_stats[depth]["cache_hits"] += 1

        if cached_result:
            cache_stats["true_hits"] += 1
        else:
            cache_stats["false_hits"] += 1

        return cached_result

    # --------------------------------------------------------
    # CACHE MISS
    # --------------------------------------------------------

    cache_stats["misses"] += 1
    depth_stats[depth]["cache_misses"] += 1

    d_max = (x - min_value) // (k - 1)

    # --------------------------------------------------------
    # CHECK POSSIBLE COMMON DIFFERENCES
    # --------------------------------------------------------

    for d in range(1, d_max + 1):

        progression_found = True

        for i in range(1, k):

            previous_value = x - i * d

            bit = value_bit(previous_value)

            if not (current_mask & bit):
                progression_found = False
                break

        if progression_found:

            kap_cache[key] = True
            cache_stats["true_stores"] += 1

            return True

    # --------------------------------------------------------
    # NO PROGRESSION FOUND
    # --------------------------------------------------------

    kap_cache[key] = False
    cache_stats["false_stores"] += 1

    return False


