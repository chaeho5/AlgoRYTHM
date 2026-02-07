import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();

        int[][] arr = new int[9][9];
        int max = 0;
        for(int i = 0; i < 9; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 9; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int x = 0;
        int y = 0;

        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                if(arr[i][j] > max){
                    max = arr[i][j];
                    x = i;
                    y = j;
                }
            }
        }

        System.out.println(max);
        System.out.print((x + 1) + " " + (y + 1));
    }
}
