#include <iostream>
#include <queue>
#include<string.h>
using namespace std;

int N, M;
int arr[101];
bool visit[101];
	
int main(void)
{
	cin >> N >> M;
	for (int i = 0; i < N + M; i++)
	{
		int a, b;
		cin >> a >> b;
		arr[a] = b;
	}
	
	visit[1] = true;
	queue<pair<int, int> > que;
	que.push({ 1,0 });


	while (!que.empty())
	{
		int idx = que.front().first;
		int cur = que.front().second;
		que.pop();

		if (idx == 100)
		{
			cout << cur << endl;
			break;
		}

		for (int i = 1; i <= 6; i++)
		{
			if (idx + i <= 100)
			{
				if (arr[idx + i])
				{
					if (!visit[arr[idx + i]])
					{
						visit[arr[idx + i]] = true;
						que.push({ arr[idx + i], cur + 1 });
					}
				}
				else
				{
					if (!visit[idx + i])
					{
						visit[idx + i] = true;
						que.push({ idx + i, cur + 1 });
					}
				}
			}

		}
	}
	

}



