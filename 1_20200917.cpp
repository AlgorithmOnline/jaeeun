#include<iostream>
#include<algorithm>
#include<string.h>
#include<queue>
#include<stack>
#include<vector>
using namespace std;
#define MOD 1000000007
long long num[1000001];
long long tree[3000001];


long long init(int n, int s, int e)
{
	if (s == e)
	{
		tree[n] = num[s];
		return tree[n];
	}
	int m = (s + e) / 2;
	tree[n] = ( (init(2 * n, s, m) % MOD) * (init(2 * n + 1, m + 1, e)% MOD) )%  MOD;
	return tree[n];
}

void update(int n, int s, int e, int t, int diff)
{
	if (t < s || e < t)
	{
		return;
	}

	if (s == e)
	{
		tree[n] = diff;
		return;
	}
	int m = (s + e) / 2;
	update(2 * n, s, m, t, diff);
	update(2 * n + 1, m + 1, e, t, diff);
	tree[n] = (tree[n * 2] * tree[n * 2 + 1]) % MOD;
}

long long mul(int n, int s, int e, int l, int r)
{
	if (l <= s && e <= r)
	{
		return tree[n];
	}

	if (r < s || e < l)
	{
		return 1;
	}

	int m = (s + e) / 2;
	return (mul(2 * n, s, m, l, r) * mul(2 * n + 1, m + 1, e, l, r)) % MOD;
}

int main()
{
	int N, M, K;
	cin >> N >> M >> K;
	for (int i = 1; i <= N; i++)
	{
		cin >> num[i];
	}
	init(1, 1, N);
	for (int i = 0; i < M + K; i++)
	{
		int a, b, c;
		cin >> a >> b >> c;
		if (a == 1)
		{
			num[b] = c;
			update(1, 1, N, b, c);
		}
		else
		{
			cout << mul(1, 1, N, b, c) % 1000000007 << endl;
		}
	}
}
