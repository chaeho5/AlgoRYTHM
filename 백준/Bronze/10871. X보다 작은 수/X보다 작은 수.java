import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer nx = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(nx.nextToken());
        int X = Integer.parseInt(nx.nextToken());
        StringTokenizer num = new StringTokenizer(br.readLine(), " ");
        int[] A = new int[N];
        ArrayList<Integer> result = new ArrayList<>();

        for(int i = 0; i < N; i++){
            A[i] = Integer.parseInt(num.nextToken());
            if(A[i] < X){
                result.add(A[i]);
            }
        }

        for(int n : result){
            System.out.print(n + " ");
        }
    }
}
