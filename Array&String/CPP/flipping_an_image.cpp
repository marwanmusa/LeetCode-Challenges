#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        for (int i = 0; i < image.size(); i++) {
            vector<int> temp = image[i];
            reverse(temp.begin(), temp.end());
            image.at(i) = inverse(temp);
        }
        return image;
    }

    vector<int> inverse(vector<int> arr) {
        for (int i = 0; i < arr.size(); i++) {
            arr[i] = abs(arr[i]-1);
        }
        return arr;
    }
};