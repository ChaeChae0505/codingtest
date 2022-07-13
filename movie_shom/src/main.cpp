#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
  int n;
  int cnt = 0;
  cin >> n;
  int six = 666;

  while(cnt != n){
    if(to_string(six).find("666") != string::npos){
      cnt++;
    }
    six++;
  }
  cout << six -1;
  return 0;
}
