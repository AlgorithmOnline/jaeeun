#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector v;

int main(void)
{
string ins;
int N;
cin>>N;

for(int i=0; i<N; i++)
{
cin>>ins;

if(ins == "push")
{  
  int x;
  cin>>x;
  v.push_back(x);
}
else if(ins == "top")
{

int size = v.size()-1;
if(!v.empty())
{
cout<<v[size]<<endl;

}
else{
cout<<-1<<endl;
}

}
else if(ins == "empty")
{
if(v.empty()){
cout<<1<<endl;
}
else{
cout<<0<<endl;
}

}
else if(ins == "size")
{
cout<<v.size()<<endl;
}
else if(ins =="pop"){

if(v.empty()){cout<<-1;
}
else{

int size = v.size()-1;
v.pop_back();
cout<<v[size]<<endl;
