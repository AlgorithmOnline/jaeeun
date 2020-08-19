#include <iostream>
using namespace std;
int main() {
	int nine_numbers[9];
	for (int i = 0; i < 9; i++) {
		cin >> nine_numbers[i];
	}
	int max = nine_numbers[0];
	int count = 0;
	for (int i = 0; i < 9; i++) {
		 if (max < nine_numbers[i]) {
			max = nine_numbers[i];
			count = i;
			continue;
		}

	}
	cout << max<<" "<<count+1;


}
