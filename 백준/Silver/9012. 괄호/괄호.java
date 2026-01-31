import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++){
            Stack<Character> stack = new Stack<>();
            String vps = br.readLine();
            boolean isVPS = true;
            for(char c : vps.toCharArray()){
                if(c == '('){
                    stack.push(c);
                } else if(c == ')'){
                    if(stack.isEmpty()){
                        isVPS = false;
                        break;
                    }
                    stack.pop();
                }
            }

            if(isVPS && stack.isEmpty()){
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }

        }
    }
}