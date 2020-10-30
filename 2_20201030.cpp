#include <string>
#include <vector>
#include <iostream>
using namespace std;
int pos;
int ans;
vector<int> num;
void DFS(int cur,int idx)
{
    if(idx == num.size() - 1)
    {
        if(cur == pos)
        {
            ans++;
        }
        return;
    }
   
        DFS(cur + num[idx + 1],idx + 1);
        DFS(cur - num[idx + 1],idx + 1);
}

int solution(vector<int> numbers, int target) {
    pos = target;
    num = numbers;
    
    DFS(num[0],0);
    DFS(-num[0],0);
    return ans;
}
