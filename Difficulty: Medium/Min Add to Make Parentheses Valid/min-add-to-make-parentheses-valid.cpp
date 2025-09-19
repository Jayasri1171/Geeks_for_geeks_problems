class Solution {
  public:
    int minParentheses(string& s) {
        // code here
        stack<char>st;
        int ans=0;
        for(int i=0;i<s.size();i++){
            if (s[i]=='('){
                st.push('(');
            }
            else{
                if(st.empty()){
                    ans+=1;
                }
                else{
                    st.pop();
                }
            }
        }
        ans+=st.size();
        return ans;
    }
};