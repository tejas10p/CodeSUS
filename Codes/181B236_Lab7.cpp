// --------------
// Varun Singh   |
// 08 - 12 - 20  |
// Testing       |
// --------------

#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define ok int
#define mod 1000000007
#define vi vector<int>
#define ll long long int

void fun(){
  int k = 0;
  cin >> k;
  cout << "This is a  bad Function\n";
}

int main (void){
  //freopen("in.txt","r",stdin);
  //freopen("out.txt","w",stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  fun();
  ok t;
  cin >> t;
  //int tcpt = t;
  //Add this comment
  while(t--){
  	//cout << "Case #" << tcpt - t << ": ";
  	ok dis,k;
  	cin >> dis >> k;
  	ll x = 0,y = 0;
  	ll turns = 0;
  	while(x*x + y*y <= dis){
		if(x <= y) x+=k;
		else y+=k;
		turns += 1;
	}
	cout << turns << "\n";
	if(turns&1) cout << "Tejas\n";
	else cout << "Vivaan\n";
  }
  return 0;
}
