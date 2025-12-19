import file_utils as fu
from functools import reduce
from operator import mul


def read_file(fname):
    return [tuple(map(int, line.split(","))) for line in fu.read_file(fname)]


def calc_distances(points):
    distances = {}
    for idx, (x1, y1, z1) in enumerate(points):
        for jdx, (x2, y2, z2) in enumerate(points[idx + 1 :], start=idx + 1):
            # no need to compute sqrt for comparison purposes
            distances[(idx, jdx)] = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    return distances


def closest_distances(distances, n=2, reverse=False):
    sorted_dists = sorted(distances.items(), key=lambda item: item[1], reverse=reverse)
    return sorted_dists[:n]


def find_cluster(clusters, point_idx):
    for cluster in clusters:
        if point_idx in cluster:
            return cluster
    return None


def calculate_clusters(points, n=10):
    clusters = set()
    distances = calc_distances(points)
    closest = closest_distances(distances, n)
    for (i, j), _ in closest:
        ci = find_cluster(clusters, i)
        cj = find_cluster(clusters, j)
        if ci and cj:
            if ci != cj:  # different clusters: merge
                new = ci.union(cj)
                clusters.remove(cj)
                clusters.remove(ci)
                clusters.add(new)
        elif ci:
            new = ci.union([j])
            clusters.remove(ci)
            clusters.add(new)  # j is not yet in a cluster, add to i's cluster
        elif cj:
            new = cj.union([i])
            clusters.remove(cj)
            clusters.add(new)  # i is not yet in a cluster, add to j's cluster
        else:
            clusters.add(
                frozenset([i, j])
            )  # neither in a cluster yet, create new cluster
    return clusters


def calculate_complete_cluster(points):
    clusters = set()
    distances = calc_distances(points)
    # large enough to include all pairs, sorted descending so we POP the closest first
    closest = closest_distances(distances, n=500_000, reverse=True)
    i, j = None, None

    while not (len(clusters) == 1 and sum(len(c) for c in clusters) == len(points)):
        (i, j), _ = closest.pop()
        ci = find_cluster(clusters, i)
        cj = find_cluster(clusters, j)
        if ci and cj:
            if ci != cj:  # different clusters: merge
                new = ci.union(cj)
                clusters.remove(cj)
                clusters.remove(ci)
                clusters.add(new)
        elif ci:
            new = ci.union([j])
            clusters.remove(ci)
            clusters.add(new)  # j is not yet in a cluster, add to i's cluster
        elif cj:
            new = cj.union([i])
            clusters.remove(cj)
            clusters.add(new)  # i is not yet in a cluster, add to j's cluster
        else:
            clusters.add(
                frozenset([i, j])
            )  # neither in a cluster yet, create new cluster
    return points[i], points[j]


def part1(fname, n=10):
    points = read_file(fname)
    clusters = calculate_clusters(points, n)
    return sorted(clusters, key=lambda c: len(c), reverse=True)[:3]


def part2(fname):
    points = read_file(fname)
    p1, p2 = calculate_complete_cluster(points)
    return p1, p2


if __name__ == "__main__":
    fname = "day08.txt"
    result = part1(fname, n=1000)
    print(f"Result for part1: {reduce(mul, [len(c) for c in result])}")
    p1, p2 = part2("day08.txt")
    print(f"Result for part2: {p1[0]*p2[0]}")
