#include <iostream>



using namespace std;
int cnt=0;
bool check=false;

int main(void)
{
	int N,C;


	cin >> N >> C;

	int arr[N];

	for(int i=0; i<N; i++)
	{
		cin >> arr[i];
	}


	for(int j=1; j<=C; j++)
	{ 
		check = false;

		for(int i=0; i<N; i++)
		{   
			if(j%arr[i] ==0)
			{
				check = true;

			}
		}
		if(check)
		{
			cnt++;
		}

	}




	cout<<cnt;

}




