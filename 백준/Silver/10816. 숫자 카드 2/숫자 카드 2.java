import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.lang.StringBuilder;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer card = new StringTokenizer(br.readLine(), " ");

        int M = Integer.parseInt(br.readLine());

        StringTokenizer cardNum = new StringTokenizer(br.readLine(), " ");

        HashMap<Integer, Integer> map = new HashMap<>();

        StringBuilder sb = new StringBuilder();

        while(card.hasMoreTokens()){
            int num = Integer.parseInt(card.nextToken());

            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        while(cardNum.hasMoreTokens()){
            int target = Integer.parseInt(cardNum.nextToken());

            sb.append(map.getOrDefault(target, 0)).append(" ");
        }

        System.out.println(sb);

    }
}
