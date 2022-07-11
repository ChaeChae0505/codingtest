#include <iostream>
#include <algorithm>

int main(int argc, char const *argv[]) {
  std::string str;
  
  std::cin >> str;
  std::sort(str.begin(), str.end(), std::greater<int>());
  
  std::cout << str;
  return 0;
}
