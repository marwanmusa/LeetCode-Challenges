#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:

    // Didn't pass the all test
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        sort(arr1.begin(), arr1.end());
        unordered_map<int, int> umap;
        for (int i = 0; i < arr2.size(); i++) {
            umap[arr2[i]] = i+1;
        }

        unordered_map<int, int> umap2;
        for (int i = 0; i < arr1.size(); i++) {
            if (umap.find(arr1[i]) != umap.end()) umap2[arr1[i]] = umap[arr1[i]] - 1;
            else umap2[arr1[i]] = arr1.size();
        }

        sort(arr1.begin(), arr1.end(), [&umap2](int a, int b) {
        return umap2.at(a) < umap2.at(b);
        });

        return arr1;
    }

    // improved implementation
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        // Create a mapping of elements in arr2 to their ranks
        unordered_map<int, int> rank;
        for (int i = 0; i < arr2.size(); i++) {
            rank[arr2[i]] = i;
        }

        // Sort arr1 based on custom comparator
        sort(arr1.begin(), arr1.end(), [&rank](int a, int b) {
            // If both elements are in arr2, compare by their rank
            if (rank.count(a) && rank.count(b)) {
                return rank[a] < rank[b];
            }
            // If only one element is in arr2, it comes first
            if (rank.count(a)) return true;
            if (rank.count(b)) return false;
            // If neither is in arr2, compare the elements normally
            return a < b;
        });

        return arr1;
    }
};