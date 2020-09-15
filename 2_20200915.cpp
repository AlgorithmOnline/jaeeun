#include <string>
#include <queue>
#include <vector>
#include <string.h>
#include <iostream>
using namespace std;


char arr[25];
bool visit[5][5];
vector <int> res;
int ans = 0;


int dy[] = { -1,1,0,0 };
int dx[] = { 0,0,-1,1 };

void DFS(int idx, int cur)
{
	if (cur == 7)
	{
		
		int cnt = 0;
		for (int i = 0; i < 7; i++)
		{
			if (arr[res[i]] == 'S')
			{
				cnt++;
			}
		}
		if (cnt >= 4)
		{
			bool check[5][5];
			memset(check, 0, sizeof(check));
			memset(visit, 0, sizeof(visit));
			for (int i = 0; i < 7; i++)
			{
				check[res[i] / 5][res[i] % 5] = true;
			}

			queue<pair<int, int> > que;
			visit[res[0] / 5][res[0] % 5] = true;
			que.push({ res[0] / 5,res[0] % 5 });

			int cnt = 0;
			while (!que.empty())
			{
				int y = que.front().first;
				int x = que.front().second;
				que.pop();

				for (int i = 0; i < 4; i++)
				{
					int newy = y + dy[i];
					int newx = x + dx[i];
					if (newy >= 0 && newy < 5 && newx >= 0 && newx < 5)
					{
						if (!visit[newy][newx] && check[newy][newx])
						{
							cnt++;
							visit[newy][newx] = true;
							que.push({ newy,newx });

						}
					}
				}
			}
			if (cnt == 6)
			{
				ans++;
			}
		}

		return;
	}

	for (int i = idx + 1; i < 25; i++)
	{
		res.push_back(i);
		DFS(i, cur + 1);
		res.pop_back();
	}
}

int main(void)
{
	for (int i = 0; i < 25; i++)
	{
		cin >> arr[i];
	}

	for (int i = 0; i < 25; i++)
	{
		res.push_back(i);
		DFS(i, 1);
		res.pop_back();
	}

	cout << ans << endl;
}
