

#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
	int N,K;
	std::ios::sync_with_stdio(false);
	cin >> N >> K;

	int arr[N];

	for(int i =0 ; i<N; i++)
	{
		cin >> arr[i];
	}

	sort(arr,arr+N);

	cout << arr[K-1];



}
