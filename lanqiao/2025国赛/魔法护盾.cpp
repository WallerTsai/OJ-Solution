#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, c, b;
    if (!(cin >> n >> c >> b)) return 0;

    vector<int> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> dp(n + 1, -1);
    dp[0] = b;

    for (int i = 1; i <= n; ++i) {
        int current_s = s[i - 1];
        int current_a = a[i - 1];
        
        vector<int> new_dp(n + 1, -1);
        for (int k = 0; k <= i; ++k) {
            
            if (dp[k] != -1) {
                int new_s = min(dp[k] + current_s, c);
                if (new_s >= current_a) {
                    new_dp[k] = max(new_dp[k], new_s);
                }
            }
            
            if (k > 0 && current_s > 0 && dp[k - 1] != -1) {
                int new_s = min(dp[k - 1] + 2 * current_s, c);
                if (new_s >= current_a) {
                    new_dp[k] = max(new_dp[k], new_s);
                }
            }
        }
        
        dp = std::move(new_dp);
    }

    for (int k = 0; k <= n; ++k) {
        if (dp[k] != -1) {
            cout << k << "\n";
            return 0;
        }
    }

    cout << -1 << "\n";
    return 0;
}