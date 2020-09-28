#include <iostream>
#include <vector>
#include<queue>
#include <string.h>
#include <map>
#include<algorithm>
using namespace std;

struct Node {
	int a;
	int b;
};
int D[100];

bool compare(Node a, Node b)
{
	return a.a < b.a;
}

int main() {
	int N;
	cin >> N;

	vector<Node> vec;
	for (int i = 0; i < N; i++)
	{
		int a, b;
		cin >> a >> b;
		vec.push_back({ a,b });
	}
	sort(vec.begin(), vec.end(), compare);

	int maxa = 0;
	for (int i = 0; i < vec.size(); i++)
	{
		D[i] = 1;
		for (int j = 0; j < i; j++)
		{
			if (vec[i].b > vec[j].b && D[i] < D[j] + 1)
			{
				D[i] = D[j] + 1;
			}
		}
		if (maxa < D[i])
		{
			maxa = D[i];
		}
	}
	cout << N - maxa << endl;


}
