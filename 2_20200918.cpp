
#include <iostream>
#include <vector>
#include <string>
using namespace std;

stack stc;
int result;

int main(void)
{

string arr;
    result = 0;

cin >> arr;

for(int i=0; i<arr.length(); i++)
{
if(arr[i]=='(')
{
stc.push(arr[i]);


}
else{

stc.pop();

if(arr[i-1] == '(')
{
result += stc.size();

}
else{

result++;
}



}


}

cout << result;





}


