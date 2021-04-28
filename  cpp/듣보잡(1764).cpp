#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int n, m;
vector<string> v, v2;

int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout.tie(NULL);

	cin >> n >> m;

	for (size_t i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		v.push_back(s);
	}

	sort(v.begin(), v.end());

	for (size_t i = 0; i < m; i++)
	{
		string s;
		cin >> s;

		if (binary_search(v.begin(), v.end(), s))
			v2.push_back(s);
	}
    sort(v2.begin(), v2.end());
	cout << v2.size() << endl;

	for (size_t i = 0; i < v2.size(); i++)
	{
		cout << v2[i] << endl;
	}

	return 0;
}