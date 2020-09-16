#include <iostream>
#include <string.h>
#include <deque>
#include<queue>
#include<vector>
#include<map>
#include <algorithm>

using namespace std;

int H, W, X, Y;
int B[600][600];
int A[300][300];
int main(void)
{
	cin >> H >> W >> X >> Y;
	
	
	for (int i = 0; i < H + X; i++)
	{
		for (int j = 0; j < W + Y; j++)
		{
			cin >> B[i][j];
			if (0 <= i && i < X && 0 <= j && j < W)
			{
				A[i][j] = B[i][j];
			}

			if (X <= i && X < H && 0 <= j && j < Y)
			{
				A[i][j] = B[i][j];
			}

			if (X <= i && X < H && Y <= j && j < W + Y)
			{
				A[i][j] = B[i][j] - A[i - X][j - Y];
			}

			if (H <= i && i < H + X && Y <= j && j < W + Y)
			{
				A[i-X][j-Y] = B[i][j];
			}

			
		}
	}
	for (int i = 0; i < H; i++)
	{
		for (int j = 0; j < W; j++)
		{
			cout << A[i][j] << " ";
		}
		cout << endl;
	}
}
