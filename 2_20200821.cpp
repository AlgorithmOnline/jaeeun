 
// 백준 16397
 

 

 

 

#include <iostream>
#include <cmath>
#include <queue>

using namespace std;


int N,T,G;
bool V[100000];


int A(int X)
{
int F;
F=X+1;
return F;
}

int B(int X)
{

int F= 2*X;
int *arr = new int[5];

for(int i=4; i>=0; i--)
{

arr[i]=F%10;
F=F/10;


}

F=2*X;

for(int i=0; i<5; i++)
{
if(arr[i]!=0)
{
F=F-pow(10,4-i);
break;
}


}

return F;


}


int main(void)
{

int test;
cin>>N>>T>>G;

V[N]=true;

if(N>99999 || G<N)
{
cout<<"ANG";
}
else
{
queue  q;
queue  cnt;
q.push(N);
cnt.push(0);
V[N]=true;
while(!q.empty()&&!cnt.empty())
{   
int number =q.front();
int count = cnt.front();

q.pop();
cnt.pop();
    
if(number == G)
{
cout<<count;
return 0;
}

if(count>T){
cout<<"ANG";
return 0;
}

if(!V[B(number)] && B(number)<=G)
{

q.push(B(number));

cnt.push(count+1);
V[B(number)]=true;
}
if(!V[A(number)] && A(number)<=G)
{
q.push(A(number));
cnt.push(count+1);
V[A(number)]=true;


}



}
cout<<"ANG";



}




}
