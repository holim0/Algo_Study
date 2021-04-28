#include <string>
#include <vector>

using namespace std;

string solution(int n)
{
    string answer = "";
    string tmp = "";
    while (1)
    {

        if (n <= 0)
        {
            break;
        }
        if (n == 1)
        {
            tmp += '1';
            break;
        }

        if (n % 3 == 0)
        {
            tmp += '4';
            n = n / 3 - 1;
        }
        else if (n % 3 == 1)
        {
            tmp += '1';
            n /= 3;
        }
        else
        {
            tmp += '2';
            n /= 3;
        }
    }

    for (int i = tmp.size() - 1; i >= 0; i--)
    {
        answer += tmp[i];
    }

    return answer;
}