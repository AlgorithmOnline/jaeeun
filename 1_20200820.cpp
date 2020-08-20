```jsx
#include <iostream>
#include <string>
using namespace std;

int main() {
	int dial2[9];
	char dial[9];
	string dial_string;
	string ans = "##";
	for (int i = 0; i < 9; i++) {
		cin >> dial2[i];
	}

	for (int i = 0; i < 9; i++) {
		// i, dial2[i];
		string t = to_string(i+1);
	//	cout << t << endl;
		dial[dial2[i] - 1] = t[0];
	}
	

	cin >> dial_string;
	for (int i = 0; i < dial_string.size(); i++) {
		try {

			switch (dial_string[i])
			{

			case 'a': {
				if (ans[ans.size() - 1] == dial[1]) {

					ans = ans + "#";
				}
				ans = ans + dial[1];

				break;
			}
			case 'b': {
				if (ans[ans.size() - 1] == dial[1]) {
					ans = ans + "#";
				}
				ans = ans + dial[1] + dial[1];

				break;
			}
			case 'c': {
				if (ans[ans.size() - 1] == dial[1]) {
					ans = ans + "#";
				}
				ans = ans + dial[1] + dial[1] + dial[1];
				break;
			}

			case 'd': {
				if (ans[ans.size() - 1] == dial[2]) {
					ans = ans + "#";
				}
				ans = ans + dial[2];
				break;
			}
			case 'e': {
				if (ans[ans.size() - 1] == dial[2]) {
					ans = ans + "#";
				}
				ans = ans + dial[2] + dial[2];
				break;
			}
			case 'f': {
				if (ans[ans.size() - 1] == dial[2]) {
					ans = ans + "#";
				}
				ans = ans + dial[2] + dial[2] + dial[2];
				break;
			}
			case 'g': {
				if (ans[ans.size() - 1] == dial[3]) {
					ans = ans + "#";
				}
				ans = ans + dial[3];
				break;
			}
			case 'h': {
				if (ans[ans.size() - 1] == dial[3]) {
					ans = ans + "#";
				}
				ans = ans + dial[3] + dial[3];
				break;
			}
			case 'i': {
				if (ans[ans.size() - 1] == dial[3]) {
					ans = ans + "#";
				}
				ans = ans + dial[3] + dial[3] + dial[3];
				break;
			}

			case 'j': {
				if (ans[ans.size() - 1] == dial[4]) {
					ans = ans + "#";
				}
				ans = ans + dial[4];
				break;
			}
			case 'k': {
				if (ans[ans.size() - 1] == dial[4]) {
					ans = ans + "#";
				}
				ans = ans + dial[4] + dial[4];

				break;
			}

			case 'l': {
				if (ans[ans.size() - 1] == dial[4]) {
					ans = ans + "#";
				}
				ans = ans + dial[4] + dial[4] + dial[4];
				break;
			}

			case 'm': {
				if (ans[ans.size() - 1] == dial[5]) {
					ans = ans + "#";
				}
				ans = ans + dial[5];
				break;
			}
			case 'n': {
				if (ans[ans.size() - 1] == dial[5]) {
					ans = ans + "#";
				}
				ans = ans + dial[5] + dial[5];
				break;
			}
			case 'o': {
				if (ans[ans.size() - 1] == dial[5]) {
					ans = ans + "#";
				}
				ans = ans + dial[5] + dial[5] + dial[5];
				break;
			}

			case 'p': {
				if (ans[ans.size() - 1] == dial[6]) {
					ans = ans + "#";
				}
				ans = ans + dial[6];
				break;
			}
			case 'q': {
				if (ans[ans.size() - 1] == dial[6]) {
					ans = ans + "#";
				}
				ans = ans + dial[6] + dial[6];
				break;
			}
			case 'r': {
				if (ans[ans.size() - 1] == dial[6]) {
					ans = ans + "#";
				}
				ans = ans + dial[6] + dial[6] + dial[6];
				break;
			}

			case 's': {
				if (ans[ans.size() - 1] == dial[6]) {
					ans = ans + "#";
				}
				ans = ans + dial[6] + dial[6] + dial[6] + dial[6];
				break;
			}
			case 't': {
				if (ans[ans.size() - 1] == dial[7]) {
					ans = ans + "#";
				}
				ans = ans + dial[7];
				break;
			}
			case 'u': {
				if (ans[ans.size() - 1] == dial[7]) {
					ans = ans + "#";
				}
				ans = ans + dial[7] + dial[7];
				break;
			}

			case 'v': {
				if (ans[ans.size() - 1] == dial[7]) {
					ans = ans + "#";
				}
				ans = ans + dial[7] + dial[7] + dial[7];
				break;
			}
			case 'w': {
				if (ans[ans.size() - 1] == dial[8]) {
					ans = ans + "#";
				}
				ans = ans + dial[8];
				break;
			}
			case 'x': {
				if (ans[ans.size() - 1] == dial[8]) {
					ans = ans + "#";
				}
				ans = ans + dial[8] + dial[8];
				break;
			}
			case 'y': {
				if (ans[ans.size() - 1] == dial[8]) {
					ans = ans + "#";
				}
				ans = ans + dial[8] + dial[8] + dial[8];
				break;
			}
			case 'z': {
				if (ans[ans.size() - 1] == dial[8]) {
					ans = ans + "#";
				}
				ans = ans + dial[8] + dial[8] + dial[8] + dial[8];
				break;
			}

			default:
				break;
			}
		}
		catch (int a) {
			cout << "";

		}

	}
	for (int i = 2; i < ans.size(); i++) {
		cout << ans[i];
	}

}
```
