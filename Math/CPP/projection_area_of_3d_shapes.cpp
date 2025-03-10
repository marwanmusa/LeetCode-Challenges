#include <vector>
using namespace std;

/**
 * @brief Solution for Projection Area of 3D Shapes (LeetCode 883)
 *
 * This solution calculates the projection area of a 3D shape represented by a grid.
 * The total projection area is the sum of:
 * 1. Top view: Count of non-zero cells in the grid
 * 2. Front view: Sum of maximum height in each row
 * 3. Side view: Sum of maximum height in each column
 *
 * Time Complexity: O(n²) where n is the size of the grid
 * Space Complexity: O(1) - using only constant extra space
 */
class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        int len = grid.size();
        int top = 0, front = 0, side = 0;

        for (int i = 0; i < len; i++) {
            int maxRow = 0, maxCol = 0;

            for (int j = 0; j < len; j++) {
                // Top view: count non-zero cells
                if (grid[i][j] > 0) {
                    top++;
                }

                // Front view: find max in each row
                maxRow = max(maxRow, grid[i][j]);

                // Side view: find max in each column
                maxCol = max(maxCol, grid[j][i]);
            }

            front += maxRow;
            side += maxCol;
        }

        return top + front + side;
    }
};