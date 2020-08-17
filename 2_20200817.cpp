 

#include <iostream>
#include <queue>
#include <string>
using namespace std;


int main(void)
{

queue queue;
int size=0;
string name;


int N;
cin>>N;

for( int i=0; i<N; i++)
{
cin>>name;

if(name == "push")
{
int x;
cin >> x;
queue.push(x);


}
else if(name == "pop")
  {  
 if(!queue.empty())
{
cout<<queue.front()<<endl;
queue.pop();
}

else {cout << -1<<endl;
}

}
else if(name == "size")
{
cout<<queue.size() << endl;
}
else if(name == "empty")
{
if(queue.empty()){
cout << 1 << endl;
}
else{
cout << 0<<endl;
}


}
else if( name == "front")
{
if(!queue.empty()){
cout <<queue.front()<<endl;
}
else{
cout << -1 <<endl;
}

}
else if( name == "back")
{
if(!queue.empty()){
cout <<queue.back()<<endl;
}
else{
cout << -1 <<endl;
}

}
}
