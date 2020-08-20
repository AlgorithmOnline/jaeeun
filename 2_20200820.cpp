#include <iostream>
#include <string>
using namespace std;

int main() {
	string dial;
	int ans = 0;
	cin >> dial;
	for (int i = 0; i < dial.size(); i++) {
		switch (dial[i])
		{
		case '1':
			ans += 2; break;
		case 'A':case 'B':case 'C':
			ans += 3; break;
		case 'D':case 'E':case 'F':
			ans += 4; break;
		case 'G':case 'H':case 'I':
			ans += 5; break;
		case 'J':case 'K':case 'L':
			ans += 6; break;
		case 'M':case 'N':case 'O':
			ans += 7; break;
		case 'P':case 'Q':case 'R':case 'S':
			ans += 8; break;
		case 'T':case 'U':case 'V':
			ans += 9; break;
		case 'W':case 'X':case 'Y': case 'Z':
			ans += 10; break;
		case '0':
			ans += 11; break;
		default:
			break;
		}

	}
	cout << ans;



}
