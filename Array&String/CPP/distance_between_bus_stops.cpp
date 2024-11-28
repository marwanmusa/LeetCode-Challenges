#include <numeric>
#include <vector>
using namespace std;

template <typename T>
vector<T> slicing(vector<T> const& v,
                  int X, int Y)
{

    // Begin and End iterator
    auto first = v.begin() + X;
    auto last = v.begin() + Y + 1;

    // Copy the element
    vector<T> vector(first, last);

    // Return the results
    return vector;
}


class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        return start < destination ? distanceStops(distance, start, destination) : distanceStops(distance, destination, start);
    }

    int distanceStops(vector<int>& distance, int start, int destination) {
        int l = 0, r = distance.size() - 1, midsum = 0, lsum = 0, rsum;
        vector<int> midslice, lslice, rslice;

        midslice = slicing(distance, start, destination-1);
        rslice = slicing(distance, destination, r);

        if (start > 0) {
            lslice = slicing(distance, l, start-1);
            lsum = accumulate(lslice.begin(), lslice.end(), 0);
        }

        midsum = accumulate(midslice.begin(), midslice.end(), 0);
        rsum = accumulate(rslice.begin(), rslice.end(), 0);
        return min(midsum, lsum + rsum);
    }

    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        int dist_clock = 0, dist_aclock = 0, size = distance.size();
        int start1 = min(start, destination), destination1 = max(start, destination);

        // Iterate through the array of distances to calculate clockwise and counterclockwise distances
        for (int i = 0; i < size; i++) {
            if (i >= start1 && i < destination1)
                dist_clock += distance[i]; // Accumulate distance for clockwise direction
            else
                dist_aclock += distance[i]; // Accumulate distance for counterclockwise direction
        }

        // Return the minimum distance between clockwise and counterclockwise paths
        return min(dist_clock, dist_aclock);
    }
};