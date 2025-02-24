class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        lsum, rsum, midsum = sum(distance[:start]), sum(distance[destination:]), sum(distance[start:destination])
        return min((midsum, lsum+rsum))

    # expand the array
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        n = len(distance)
        if start > destination:
            start, destination = destination, start
        distance += distance
        return min(sum(distance[start:destination]), sum(distance[destination: n + start]))