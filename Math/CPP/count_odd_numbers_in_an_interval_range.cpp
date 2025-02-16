class Solution {
    public:
        int countOdds(int l, int h) {
            int nums = h - l + 1, hn = nums / 2;
            bool isOdd = nums & 0x1, lOdd = l & 0x1;
            if (isOdd && lOdd) return hn + 1;
            return hn;
        }
    };