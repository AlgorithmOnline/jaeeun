#include<iostream>
#include<string>
#include<algorithm>
#include<queue>
#include<vector>
#include<cmath>
#include<stack>
using namespace std;

int arr[50];

int main() {

	for (int i = 0; i < 50; i++)
	{
		cin >> arr[i];
	}
	int t;
	cin >> t;
	int cnt = 0;
	for (int i = 0; i < 50; i++)
	{
		if (arr[i] > t)
			cnt++;
	}
	cnt++;
	if (cnt <= 5)
		cout << "A+";
	else if (cnt <= 15)
		cout << "A0";
	else if (cnt <= 30)
		cout << "B+";
	else if (cnt <= 35)
		cout << "B0";
	else if (cnt <= 45)
		cout << "C+";
	else if (cnt <= 48)
		cout << "C0";
	else
		cout << "F";
	
}
