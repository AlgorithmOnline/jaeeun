#include<iostream>
#include<string>
#include<algorithm>
#include<queue>
#include<vector>
#include<cmath>
#include<stack>
using namespace std;

int N, M, K;
char arr[50][50];
int maxa;

int count()
{
	int cnt = 0;
	for (int i = 0; i < N; i++)
	{
		bool flag = true;
		for (int j = 0; j < M; j++)
		{
			if (!arr[i][j])
			{
				flag = false;
				break;
			}
		}
		if (flag)
			cnt++;
	}
	return cnt;
}




int main() {

	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> arr[i][j];
		}
	}
	cin >> K;

	int ans = 0;
	//i번째 행의 0을 다 킨다고 했을 때.

	for (int i = 0; i < N; i++)
	{
		int zero = 0;
		for (int j = 0; j < M; j++)
			if (arr[i][j] == '0')
				zero++;

		int res = 0;
		//0의 개수가 k보다 작아야 다 킬 수 있음.
		//그리고 0의 개수와 k의 개수는 짝/홀이 일치해야 함. => 아니면 다 못킴
		if (zero <= K && zero % 2 == K % 2)
		{
			//현재 행과 동일한 행의 경우 다 채워짐.
			for (int n = 0; n < N; n++)
			{
				bool flag = true;
				for (int m = 0; m < M; m++)
				{
					if (arr[i][m] != arr[n][m])
					{
						flag = false;
						break;
					}
				}
				if (flag)
					res++;
			}
		}
		//i번째를 한줄로 완성시켰을 때 res값
		ans = max(ans, res);
	}
	cout << ans << endl;
	
}
