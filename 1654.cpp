#include <iostream>
#include <algorithm>
#define MAX 10000 + 5

using namespace std;

int main()
{

    int K, N;
    long long arr[MAX];
    long long answer = -1;

    cin >> K >> N;

    for (int i = 0; i < K; i++)
    {
        cin >> arr[i];
    }

    sort(arr, arr + K);

    long long l = 1;
    long long r = arr[K - 1];
    long long mid;
    long long tmp = 0;
    while (1)
    {
        tmp = 0;
        mid = (l + r) / 2;

        for (int i = 0; i < K; i++)
        {
            tmp += arr[i] / mid;
        }

        if (tmp >= N)
        {
            l = mid + 1;
            answer = max(answer, mid);
        }
        else
        {
            r = mid - 1;
        }

        if (l > r)
        {
            break;
        }
    }

    cout << answer << endl;
    return 0;
}