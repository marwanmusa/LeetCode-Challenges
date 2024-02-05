class Solution {
    // Given an integer x, return true if x is a palindrome, and false otherwise.
public:
    bool isPalindrome(int x) {
        if (x >= 0) {
            int num = x;
            long int rev_num = 0;

            while (num != 0) {
                int digit = num % 10;
                rev_num = rev_num * 10 + digit;
                num /= 10;
            }
            return (x == rev_num);
        } else {
            return false;
        }
    }
};
