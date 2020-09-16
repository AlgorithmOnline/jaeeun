#include <iostream>
#include <string.h>
#include <deque>
#include<queue>
#include<vector>
#include<map>
#include <algorithm>

using namespace std;
priority_queue<int,vector<int>,less<int> > max_heap;
priority_queue<int,vector<int>, greater<int> > min_heap;


int main(void)
{
	int N;
	cin >> N;
	vector<int> vec;
	for (int i = 0; i < N; i++)
	{
		int a;
		scanf("%d", &a);
		if (max_heap.size() + 1 ==  min_heap.size() || max_heap.size() + 1 == min_heap.size() + 1)
		{
			max_heap.push(a);
		}
		else
		{
			min_heap.push(a);
		}

		if (max_heap.size() && min_heap.size() && max_heap.top() > min_heap.top())
		{
			int temp = max_heap.top();
			max_heap.pop();
			int temp2 = min_heap.top();
			min_heap.pop();
			max_heap.push(temp2);
			min_heap.push(temp);
		}

		printf("%d\n", max_heap.top());
	}
}


