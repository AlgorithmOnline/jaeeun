#include <string>
#include <vector>
#include<iostream>

using namespace std;
int mina = 987654321;
int res = 0;
vector<string> vec;
string pos;
bool visit[50];
bool check(string pattern,string parent)
{
    int cnt = 0;
    for(int i = 0; i < pattern.size(); i++)
    {
        if(pattern[i] != parent[i])
        {
            cnt++;
            if(cnt > 1)
                break;
        }
    }
    if(cnt == 1)
        return true;
    return false;
}

void DFS(string cur)
{
    if(res > mina)
        return;
    
    if(cur == pos)
    {
        if(mina > res)
            mina = res;
        return;
    }
    for(int i = 0; i < vec.size(); i++)
    {
        if(visit[i])
            continue;
        if(check(cur,vec[i]))
        {
            visit[i] = true;
            res++;
            DFS(vec[i]);
            res--;
            visit[i] = false;
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    vec = words;
    pos = target;
    for(int i = 0; i < words.size(); i++)
    {
        if(check(begin,words[i]))
        {
            visit[i] = true;
            res++;
            DFS(words[i]);
            res--;
            visit[i] = false;
        }
    }
    if(mina == 987654321)
        return 0;
    answer = mina;
    return answer;
}
