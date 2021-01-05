#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main()
{
	/*

	벡터

	설치
	#include <vector>

	1) iterator( 반복자)
	- begin() : beginning iterator 반환
	- end() :   end iterator 반환

	2) 추가 및 삭제
	- push_back(element) : 벡터 제일 뒤에 원소를 추가
	- pop_back(): 벡터 제일 뒤에 원소 삭제

	3) 조회
	- [i] : i 번째 원소를 반환
	- at(i) :  i 번째 원소를 반환
	- front() : 첫 번째 원소를 반환
	- back(): 마지막 원소를 반환

	4) 기타
	- empty() : 벡터가 비어있으면 true 아니면 false를 반환
	- size(): 벡터 원소들의 수를 반환

	5) 배열과의 차이
	동적으로 원소를 추가할 수 있고, 크기가 자동으로 늘어난다.

 */
	int N;
	string command;
	vector<int> v;
	cin >> N;
	for (int i = 0; i < N; i++) {

		cin >> command;
		// string 은 그냥 if 문 쓰는게 낫다는 결론


		if (command == "push") {

			// c++은 string 은 무조건 "" 사용

			int n;
			cin >> n;
			v.push_back(n);
			continue;
		}

		else if (command == "pop") {
			if (v.empty()) {
				cout << -1 << "\n";

			}
			else {
				cout<< v.back();
				v.pop_back();
				cout << "\n";
			}
			continue;
		}

		else if (command == "size") {
			cout << v.size() << "\n"; continue;
		}
		else if (command == "empty") {
			int isempty = (v.empty()) ? 1 : 0;
			cout << isempty << "\n"; continue;

		}
		else if (command == "top") {
			int istop = (v.empty()) ? -1 : v.back();
			cout << istop<<"\n"; continue;
		}

	}





}

