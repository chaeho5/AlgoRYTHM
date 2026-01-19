import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        String A = st.nextToken();
        String reverseA ="";
        String B = st.nextToken();
        String reverseB = "";

        for(int i = A.length() - 1; i >= 0; i--){
            char a = A.charAt(i);
            reverseA += a;

            char b = B.charAt(i);
            reverseB += b;
        }

        int ra = Integer.parseInt(reverseA);
        int rb = Integer.parseInt(reverseB);

        int result = Math.max(ra, rb);

        System.out.println(result);
    }
}
