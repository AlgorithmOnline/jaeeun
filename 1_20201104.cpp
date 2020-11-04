#include <iostream>
#include<vector>
#include <algorithm>
#include<cmath>
#include<queue>
using namespace std;
#define ll long long

int CCW(pair<ll, ll> p1, pair<ll, ll> p2, pair<ll, ll> p3)
{
	ll temp = p1.first * p2.second + p2.first * p3.second + p3.first * p1.second;

	temp = temp - p1.second * p2.first - p2.second * p3.first - p3.second * p1.first;

	if (temp > 0) return 1; // 반시계
	else if (temp == 0) return 0; // 일직선
	else if (temp < 0) return -1; // 시계
}

int main() {

	
	pair<int, int> A;
	pair<int, int> B;
	pair<int, int> C;
	pair<int, int> D;
	cin >> A.first >> A.second;
	cin >> B.first >> B.second;
	cin >> C.first >> C.second;
	cin >> D.first >> D.second;
	
	//ABC
	int abc = CCW(A,B,C);
	//ABD
	int abd = CCW(A,B,D);
	//CDA
	int cda = CCW(C,D,A);
	//CDB
	int cdb = CCW(C,D,B);

	if (abc * abd == 0 && cda * cdb == 0)
	{
		if (A > B)swap(A, B);
		if (C > D)swap(C, D);
		//first 비교가 아닌 것은 x가 같고 y가 달라서 일직선일 수 있으므로..
		if (A <= D && C <= B)
		{
			cout << 1 << endl;
		}
		else
		{
			cout << 0 << endl;
		}
		return 0;
	}
	

	if (abc * abd <= 0 && cda * cdb <= 0)
	{
		cout << 1 << endl;
	}
	else
		cout << 0 << endl;
}
