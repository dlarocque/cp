class Solution {
public:
    bool isValid(string s) {
        stack<char> parens;
        for(char& c : s) {
            switch(c) {
                case '(':
                case '{':
                case '[':
                    parens.push(c);
                    break;
                case ')':
                    if(parens.empty() || parens.top() != '(')
                        return false;
                    else
                        parens.pop();
                        break;
                case '}':
                    if(parens.empty() || parens.top() != '{')
                        return false;
                    else
                        parens.pop();
                        break;
                case ']':
                    if(parens.empty() || parens.top() != '[')
                        return false;
                    else
                        parens.pop();
                        break;
            }
        }
        return parens.empty();
    }
};
