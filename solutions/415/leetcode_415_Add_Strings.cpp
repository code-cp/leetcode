#include<iostream>
#include<string>

using namespace std; 

class Solution {
public:
    string addStrings(string num1, string num2) {
        if (num1.length() < num2.length())
            swap(num1, num2);
        num1 = "0" + num1; 
        int l1 = num1.length();
        int l2 = num2.length();
        for (int i = 0; i < l1-1; ++i)
        {
            if (i < l2)
                num1[l1 - i - 1] += (num2[l2 - i - 1] - '0');
            if (num1[l1 - i - 1] > '9')
            {
                // 注意这里不是'10' !! 
                num1[l1 - i - 1] -= 10;
                ++num1[l1 - i - 2];
            }
            cout << num1 << endl;
        }
        return (num1[0] != '0') ? num1 : num1.substr(1);
    }
};

int main()
{
    Solution s; 
    string num1 = "1";
    string num2 = "9";
    string ans = s.addStrings(num1, num2);
    cout << ans << endl; 
}