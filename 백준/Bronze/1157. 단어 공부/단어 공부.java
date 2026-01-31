import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        HashMap<Character, Integer> map = new HashMap<>();

        for(char c : str.toUpperCase().toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        int maxCount = -1;
        char answer = '?';

        for(char key : map.keySet()){
            if(maxCount < map.get(key)){
                maxCount = map.get(key);
                answer = key;
            }else if(map.get(key) == maxCount){
                answer = '?';
            }
        }
        System.out.println(answer);
    }
}
