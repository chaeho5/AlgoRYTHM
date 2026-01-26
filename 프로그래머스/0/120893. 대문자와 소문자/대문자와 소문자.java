class Solution {
    public String solution(String my_string) {
        String answer = "";
        for (int i = 0; i < my_string.length(); i++){
            char c = my_string.charAt(i);
            if(c >= 'a' && c <= 'z'){
                char bc = Character.toUpperCase(c);
                answer += bc;
            } else {
                char sc = Character.toLowerCase(c);
                answer += sc;
            }
        }
        
        return answer;
    }
}