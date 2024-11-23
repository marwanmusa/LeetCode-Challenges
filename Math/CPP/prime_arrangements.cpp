#include <cmath>
#include <vector>
using namespace std;

class Solution {
public:
    int divisor = pow(10, 9) + 7;
    int numPrimeArrangements(int n) {
        int prime = SieveOfEratosthenes(n);
        int nonPrime = n - prime;
        return (factorial(nonPrime) * factorial(prime)) % divisor;
    }

    long long factorial(int n) {
        long long res = 1;
        for (int i = 2; i <= n; i++) res = (res * i) % divisor;
        return res;
    }

    int SieveOfEratosthenes(const int n) {
        vector<bool> prime(n+1, true);
        int p = 2;
        while (p * p <= n) {
            if (prime[p] == true) {
                for (int i = p * p; i <= n; i += p) prime[i] = false;
            }
            p++;
        }
        int cnt = 0;
        for (int i = 2; i <= n; i++) {
            if (prime[i] == true) cnt++;
        }
        return cnt;
    }
};