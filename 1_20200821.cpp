//백준 1260
#include <iostream>
using namespace std;
int N,F,V;
int tree[1001][1001];
int visit[1001];
int visitb[1001];

void DFS(int v)
{ 
cout<<v<<" ";


for(int i=1; i<=N; i++)
{
if(tree[v][i]==1 &&!visit[i])
{  
visit[i]=1;
 DFS(i);
}
}
   
}
void BFS(int v)
{    int k;
if(!visitb[v]){
cout<<v<<" ";
visitb[v]=1;
}

int min =1000;
for(int i=1; i<=N; i++)
{
if(tree[v][i]==1 &&!visitb[i])
{   
     cout<<i<<" ";
visitb[i]=1;
 if(i<min){
  min=i;
 }
}
}
if(min!=1000)
{
BFS(min);
    }
}


int main(void)
{





int Start,End;

cin>>N>>F>>V;
   
    
for(int i=0; i<N; i++)
 for(int j=0; j<N; j++)
 {
  tree[i][j]=0;
 }

for(int i=0;i<F;i++)
{
cin>>Start>>End;
tree[Start][End]=1;
        tree[End][Start]=1;
}
    visit[V]=1;
DFS(V);
cout<<endl;
BFS(V);


}
