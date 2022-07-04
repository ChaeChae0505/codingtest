#include <iostream>

int main(){
    std::string str;

    int n;
    int cnt = 0;
    
    std::cin >> n;

    for(int i=0; i<n; i++){
        bool flag = true;

        std::cin >> str;
        int len = str.length();
        for(int j=0; j<len; j++){
            for(int k=0; k<j; k++){
                if(str[j] != str[j-1] && str[j] == str[k]){
                    flag = false;
                    break;
                }
            }
        }
        if(flag) cnt++;
    }
    
    std::cout << cnt;

    return 0;

}