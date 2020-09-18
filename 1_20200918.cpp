#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int white, black, length;
bool check = false;

struct node{

int wc;
int bc;
int lc;

bool operator<(node const &e)
{
return lc > e.lc;
    }
};

vector <node>vec;


int main(void)
{


int N,w,b;
string str;

cin >> N >> b >> w;

cin >> str;

for(int i=0; i< str.size(); i++)
{
 white = 0;
 black = 0;
 length = 0;

for(int j = i; j < str.size(); j++)
{   

if(str[j] == 'W')
{
white++;
length++;
}
else if(str[j] == 'B')
{
black++;
length++;
}

if(black>b)
{   
    black--;
length--;
break;
}

}
vec.push_back({white,black,length});


}

sort(vec.begin(),vec.end());



for(int i =0; i < vec.size(); i++)
{
if(vec[i].wc>=w)
{
cout << vec[i].lc<<endl;
check = true;
break;

}

}
if(!check){
cout<<"0"<<endl;
}



}
