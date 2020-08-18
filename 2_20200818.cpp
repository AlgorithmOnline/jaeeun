#include <iostream>
#include  <string>

using namespace std;

int main(void)
{
 string str;
 int cnt=1;
 
cin>>str;
    for(int i=0; i<100; i++)
    {
     if(str[i]==','){
 cnt++;
}
    
}

cout<<cnt;


return 0;




}
