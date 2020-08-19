#include <iostream>
#include <string>
using namespace std;
int main()
{
	int row = 8;
	int ans = 0;
	for (int irow = 0; irow < row; irow++) {
		string one_row;
		cin >> one_row;
		for (int i = 0; i < 8; i++) {
			if ((i % 2 == 0 && irow %2 ==0)|| (i % 2 == 1 && irow % 2 == 1)) {
				if (one_row[i] == 'F')
				{
					ans++;
					continue;
				}
			}
			else {
				continue;
			}
		}
	}

	cout << ans;

}
