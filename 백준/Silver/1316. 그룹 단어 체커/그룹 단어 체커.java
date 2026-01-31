
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int count = 0;

        for(int i = 0; i < N; i++) {
            String word = br.readLine();

            boolean[] check = new boolean[26];
            char prev = ' ';
            boolean isGroupWord = true;

            for (char c : word.toCharArray()) {
                if (prev != c) {
                    if (check[c - 'a'] == true) {
                        isGroupWord = false;
                        break;
                    }
                    check[c - 'a'] = true;
                    prev = c;
                }
            }
            
            if(isGroupWord){
                count ++;
            }
        }

        System.out.println(count);
    }
}