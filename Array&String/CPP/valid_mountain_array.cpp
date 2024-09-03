#include <vector>
using namespace std;

class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        if ((arr.size() < 3) || (arr[0] > arr[1])) return false;
        
        bool valley = false;
        int cur = arr[0];
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] == cur) return false;
            else if (arr[i] < cur) {
                valley = true;
                cur = arr[i];
            }
            else {
                if (valley) return false;
                else cur = arr[i];
            }
        }
        return (!valley) ? false : true;
    }

    // move index only
    bool validMountainArray2(vector<int>& arr) {
        int i = 0, j = arr.size()-1;
        if ((arr.size() < 3) || (arr[0] > arr[1])) return false;
        while (i < arr.size()-1 && arr[i] < arr[i+1]) i++;
        while (j > 0 && arr[j] < arr[j-1]) j--;
        return 0 < i && i == j && j < arr.size()-1;
    }
};