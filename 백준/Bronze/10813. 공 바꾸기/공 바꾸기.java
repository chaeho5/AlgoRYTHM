import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int temp = 0;
        int[] basket = new int[N];

        for (int i = 0; i < N; i++){
            basket[i] = i + 1;
        }

        for (int i = 0; i < M; i++){
            StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
            int first = Integer.parseInt(st2.nextToken()) - 1;
            int second = Integer.parseInt(st2.nextToken()) - 1;

            temp = basket[first];
            basket[first] = basket[second];
            basket[second] = temp;
        }

        for (int i = 0; i < N; i++){
            System.out.print(basket[i] + " ");
        }


    }
}
