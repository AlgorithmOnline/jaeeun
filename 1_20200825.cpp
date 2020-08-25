#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int parent[100000];
int size[100000];

int findparent(int Node)
{
if(parent[Node]==Node)
return Node;


return parent[Node]=findparent(parent[Node]);


}

void merge(int A, int B)
{   
   
    int node1=findparent(A);
    int node2=findparent(B);
    
       if (size[node1] < size[node2])
       {
  
       
         parent[node1] = node2; //node2 집합이 node1에 합쳐짐

            size[node2] += size[node1]; //node1의 집합 크기가 커짐

            size[node1] = 0; 

           }
      else if(size[node1]>=size[node2])
      {
       parent[node2] = node1; //node2 집합이 node1에 합쳐짐

            size[node1] += size[node2]; //node1의 집합 크기가 커짐

            size[node2] = 0; 
      
  }


}

struct Node{

int x;
int y;
int weight;

bool operator<(Node const &e)
{

return weight < e.weight;

}

};

int main(void)
{


 int V,E;
 
 cin >> V >> E;
 

    vector edge;
    
 for(int i=0 ; i <E; i++)
 {
  int a, b, c;
  cin >> a >> b >> c;
 
 edge.push_back({a,b,c});
 }
 
 
 for(int i=0 ; i<V; i++)
 {
  parent[i]=i;
  size[i]=1;
 
 }
 

  sort(edge.begin(),edge.end());
 
 
 int result=0;
 
  for(int j=0; j<edge.size(); j++)
  {
  if(findparent(edge[j].x)!=findparent(edge[j].y))
  {
  merge(edge[j].x,edge[j].y);
  result +=  edge[j].weight;
 
 }
 
 }
 
 cout << result;
 
 


}
