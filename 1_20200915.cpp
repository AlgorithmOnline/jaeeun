#include <iostream>
#include <string.h>
#include <deque>
#include<queue>
#include<vector>
#include<map>
#include <algorithm>

using namespace std;

int N, M;
char arr[1001][1001];
int check[1001][1001];
int group[1001][1001];
vector<int> gcount;

map<int, bool> visit;

int dy[] = { -1,1,0,0 };
int dx[] = { 0,0,-1,1 };

struct Node
{
	int y;
	int x;
};

int main(void)
{
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> arr[i][j];
		}
	}
	memset(group, -1, sizeof(group));
	int idx = 0;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (arr[i][j] == '0' && group[i][j] == -1)
			{
				queue<Node> que;
				que.push({ i,j });
				group[i][j] = idx;

				int count = 1;
			
				while (!que.empty())
				{
					int y = que.front().y;
					int x = que.front().x;
					que.pop();
					
					for (int k = 0; k < 4; k++)
					{
						int newy = y + dy[k];
						int newx = x + dx[k];
						if (newy >= 0 && newy < N && newx >= 0 && newx < M)
						{
							if (group[newy][newx] == -1 && arr[newy][newx] == '0')
							{
								count++;
								group[newy][newx] = idx;
								que.push({ newy,newx });
							}
						}
					}
				}
				gcount.push_back(count);
				idx++;
			}
		}
	}
	

	

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (arr[i][j] == '1')
			{
				int c = 1;
				visit.clear();
				for (int k = 0; k < 4; k++)
				{
					int newy = i + dy[k];
					int newx = j + dx[k];
					if (newy >= 0 && newy < N && newx >= 0 && newx < M)
					{
						if (group[newy][newx] != -1 && !visit[group[newy][newx]])
						{
							visit[group[newy][newx]] = true;
							c += gcount[group[newy][newx]];
						}
					}
				}
				c %= 10;
				check[i][j] = c;
			}
		}
	}
	


	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cout << check[i][j] ;
		}
		cout << endl;
	}

}
