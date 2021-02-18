#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using std::cin;
using std::cout;
using std::endl;

int main()
{
    std::vector<int> v;
    int n, input;
    cin >> n;

    while (cin >> input)
        v.push_back(input);

    sort(v.begin(), v.end(), std::less<int>());

    for (auto x : v)
        cout << x << ' ';
    return 0;
}
