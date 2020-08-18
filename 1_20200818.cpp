
#include <iostream>
#include  <deque>
#include  <string>
using namespace std; 


int main(void) 
{ 

deque <int> de; 
string name; 


int N; 
cin>>N; 

for( int i=0; i<N; i++) 
{ 
cin>>name; 

if(name == "push_front") 
{ 
int x; 
cin >> x; 
de.push_front(x); 


} 
else if(name == "push_back") 
{ 
int x; 
cin >> x; 
de.push_back(x); 


} 
else if(name == "pop_front") 
  {   
 if(!de.empty()) 
{ 
cout<<de.front()<<endl; 
de.pop_front(); 
} 

else {cout << -1<<endl; 
} 

} 
else if(name == "pop_back") 
  {   
 if(!de.empty()) 
{ 
cout<<de.back()<<endl; 
de.pop_back(); 
} 

else {cout << -1<<endl; 
} 

} 
else if(name == "size") 
{ 
cout<<de.size() << endl; 
} 
else if(name == "empty") 
{ 
if(de.empty()){ 
cout << 1 << endl; 
} 
else{ 
cout << 0<<endl; 
} 


} 
else if( name == "front") 
{ 
if(!de.empty()){ 
cout <<de.front()<<endl; 
} 
else{ 
cout << -1 <<endl; 
} 

} 
else if( name == "back") 
{ 
if(!de.empty()){ 
cout <<de.back()<<endl; 
} 
else{ 
cout << -1 <<endl; 
} 

} 
}

}
