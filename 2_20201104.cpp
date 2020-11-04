#include <iostream>
#include<vector>
#include <algorithm>
#include<cmath>
#include<queue>
using namespace std;


long long CCW(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3)
{
	long long a = x1 * y2 + x2 * y3 + x3 * y1;
	long long b = y1 * x2 + y2 * x3 + y3 * x1;
	if (a - b < 0)
	{
		return 1;
	}
	else
	{
		return -1;
	}
}

int main() {

	int x1, x2, x3, x4 , y1, y2, y3, y4;
	cin >> x1 >> y1 >> x2 >> y2;
	cin >> x3 >> y3 >> x4 >> y4;
	
	//ABC
	long long abc = CCW(x1, y1, x2, y2, x3, y3);
	//ABD
	long long abd = CCW(x1, y1, x2, y2, x4, y4);
	//CDA
	long long cda = CCW(x3, y3, x4, y4, x1, y1);
	//CDB
	long long cdb = CCW(x3, y3, x4, y4, x2, y2);

	if (abc * abd <= 0 && cda * cdb <= 0)
	{
		cout << 1 << endl;
	}
	else
		cout << 0 << endl;
}
