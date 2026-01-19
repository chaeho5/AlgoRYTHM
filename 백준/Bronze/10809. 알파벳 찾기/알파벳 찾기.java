import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String S = br.readLine();
        int[] arr = new int[26];

        for (int i = 0; i < 26; i++){
            arr[i] = -1;
        }
        for (int i = 0; i < S.length(); i++){
            char c = S.charAt(i);
            int alpha = c - 'a';

            if(arr[alpha] == -1 ) {
                arr[alpha] = i;
            }
        }
        for(int i = 0; i < 26; i++){
            System.out.print(arr[i] + " ");
        }
    }
}
