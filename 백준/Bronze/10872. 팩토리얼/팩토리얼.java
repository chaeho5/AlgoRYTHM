import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int result = facto(N);

        System.out.println(result);
    }
    public static int facto(int N){
        if(N <= 1) {
            return 1;
        }

        return N * facto(N - 1);
    }
}
