#include <iostream>
using namespace std;


int V,E,K;
int arr[20000][20000];

const int INF =1000000;


int getshort(int *d, int *visit)
{

	int index;
	int min = 1000000;

	for(int i=0; i<V; i++)
	{

		if(!visit[i] && d[i]<min)
		{
			min=d[i];
			index =i;
		}

	}

	visit[index]=true;
	return index;

}


void dijkstra(int start,int *d, int *visit)
{

	visit[start] = true;

	for(int i = 0; i<V; i++ )
	{ 
		d[i] = arr[start][i];
	}

	d[start] = 0;

	for(int i= 0 ; i<V-2; i++)
	{
		int current = getshort(d,visit);

		for(int j =0; j<V; j++)
		{
			if(!visit[j])
			{
				if(d[current]+arr[current][j] < d[j] )
				{

					d[j] = d[current]+arr[current][j];
				}
			}
		}

	}



}


int main(void)
{



	cin >> V >>E;
	cin>>K;




	int d[V];
	int visit[V];


	for(int i=0; i<V; i++)
		for(int j=0; j<V; j++)
		{
			arr[i][j] =INF;
		}

	for(int i=0; i<E; i++)
	{
		int a,b,c;

		cin >>a>>b>>c;

		arr[a-1][b-1]=c;


	}

	dijkstra(K-1,d,visit);

	for(int i =0; i<V; i++)
	{

		if(d[i] == INF)
		{
			cout<<"INF"<<endl;

		}
		else
		{
			cout<<d[i]<<endl;
		}

	}




}
