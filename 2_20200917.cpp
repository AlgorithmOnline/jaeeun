#include<iostream>
#include<algorithm>
#include<string.h>
#include<queue>
#include<stack>
#include<vector>
using namespace std;

stack<pair<int,int> > sta;


int main()
{
	int N;
	int idx = 0;
	long long ans = 0;



	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int a;
		cin >> a;
		pair<int, int> p = { a,1 };
		int same = 0;
		while (!sta.empty())
		{
			if (sta.top().first <= p.first)
			{
				ans += sta.top().second;
				if (sta.top().first == p.first)
				{
					p.second += sta.top().second;
				}
				sta.pop();
			}
			else
			{
				ans++;
				break;
			}
		}
		sta.push(p);
		
	}
	cout << ans << endl;
}
