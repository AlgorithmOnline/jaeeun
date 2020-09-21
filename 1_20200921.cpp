#include <stdio.h>
#include <iostream>
using namespace std;
struct Node{
    Node *child[26];
    int cnt;
};

Node *root = (Node *)malloc(sizeof(Node));

void init(void) {
    root->cnt = 0;
    for(int i = 0; i < 26; i++)
    {
        root->child[i] = 0;
    }
}

void insert(int buffer_size, char *buf) {

    Node *now = root;
    for(int i = 0; i < buffer_size; i++)
    {
        if(now->child[buf[i]-'a'])
        {
            now = now->child[buf[i]-'a'];
        }
        else
        {
            now->child[buf[i]-'a'] = (Node *)malloc(sizeof(Node));
            now = now->child[buf[i]-'a'];
            for(int j = 0; j < 26; j++)
            {
                now->child[j] = 0;
            }
            now->cnt = 0;
        }
        
        now->cnt += 1;
    }
        
}


int query(int buffer_size, char *buf) {
  
    Node *now = root;
    for(int i = 0; i < buffer_size; i++)
    {
        if(now->child[buf[i]-'a'])
        {
      		now = now->child[buf[i]-'a'];      
        }
        else
        {
            return 0;
        }
    }
    return now->cnt;
}

int main(void) {
	//freopen("input.txt", "r", stdin);
	int TestCase; 
	for (scanf("%d", &TestCase); TestCase--;) {
		int Query_N;
		scanf("%d", &Query_N);
		
		init();
		
		static int tc = 0;
		printf("#%d", ++tc);
		
		for (int i = 1; i <= Query_N; i++) {
			int type; scanf("%d", &type);

			if (type == 1) {
				char buf[15] = { 0, };
				scanf("%s", buf);
				
				int buffer_size = 0;
				while (buf[buffer_size]) buffer_size++;
				
				insert(buffer_size, buf);
			}
			else {
				char buf[15] = { 0, };
				scanf("%s", buf);
				
				int buffer_size = 0;
				while (buf[buffer_size]) buffer_size++;

				printf(" %d", query(buffer_size, buf));
			}
		}
		printf("\n");
		fflush(stdout);
	}
}

