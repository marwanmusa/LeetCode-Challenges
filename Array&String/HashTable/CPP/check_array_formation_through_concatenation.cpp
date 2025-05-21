#include <vector>
#include <unordered_map>
using namespace std;
// 1640. Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/description/

class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        unordered_map<int, int> idxs;
        int n = arr.size();
        for (int i = 0; i < n; i++) idxs[arr[i]] = i;

        int remain = n;
        for (const vector<int>& piece : pieces) {
            int piece_width = piece.size();
            if (idxs.count(piece[0]) == 0) return false;

            int prev = idxs[piece[0]];
            remain--;

            for (int j = 1; j < piece_width; j++) {
                if (idxs.count(piece[j]) == 0 || idxs[piece[j]] != ++prev)
                    return false;
                remain--;
            }
        }

        return remain == 0;
    }

    // Direct Mapping
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        unordered_map<int, vector<int>> piece_map;

        // Map the first element of each piece to the full piece
        for (const auto& piece : pieces) {
            piece_map[piece[0]] = piece;
        }

        int i = 0;
        while (i < arr.size()) {
            if (piece_map.count(arr[i]) == 0) return false;

            const vector<int>& piece = piece_map[arr[i]];
            for (int num : piece) {
                if (i >= arr.size() || arr[i] != num) return false;
                i++;
            }
        }

        return true;
    }
};