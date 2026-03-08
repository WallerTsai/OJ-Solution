#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int OFFSET = 3000000;
const int MAX_VAL = 6000005;

bool p2_vis[MAX_VAL]; 

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p0, p1;

    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        if (y == 0) {
            p0.push_back(x);
        } else if (y == 1) {
            p1.push_back(x);
        } else if (y == 2) {
            p2_vis[x + OFFSET] = true;
        }
    }

    sort(p0.begin(), p0.end());
    p0.erase(unique(p0.begin(), p0.end()), p0.end());

    sort(p1.begin(), p1.end());
    p1.erase(unique(p1.begin(), p1.end()), p1.end());

    bool found = false;

    for (int x1 : p1) {
        for (int x0 : p0) {
            int x2 = 2 * x1 - x0;
            
            if (p2_vis[x2 + OFFSET]) {
                cout << "[" << x0 << ", 0] [" << x1 << ", 1] [" << x2 << ", 2]\n";
                found = true;
            }
        }
    }

    if (!found) {
        cout << "-1\n";
    }

    return 0;
}