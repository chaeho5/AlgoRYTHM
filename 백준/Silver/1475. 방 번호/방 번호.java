import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String N = br.readLine();
        int[] count = new int[10];
        for (char c: N.toCharArray()){
            int num = c - '0';
            count[num]++;
        }

        int sum69 = count[6] + count[9];
        int set69 = (sum69 + 1) / 2;

        count[6] = set69;
        count[9] = set69;

        int max = 0;
        for(int i : count){
            if(i > max){
                max = i;
            }
        }
        System.out.println(max);
    }
}
