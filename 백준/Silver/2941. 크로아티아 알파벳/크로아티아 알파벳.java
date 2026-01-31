import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] croatia = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        String str = br.readLine();
        for(String val : croatia){
            str = str.replace(val, "!");
        }
        System.out.println(str.length());
    }
}