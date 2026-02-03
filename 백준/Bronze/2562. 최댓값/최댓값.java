import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int max = Integer.MIN_VALUE;
        int index = 0;
        for (int i = 0; i < 9; i++){
            int currentNum = Integer.parseInt(br.readLine());

            if(currentNum > max){
                index = i + 1;
                max = currentNum;
            }
        }

        System.out.println(max);
        System.out.println(index);
    }
}
