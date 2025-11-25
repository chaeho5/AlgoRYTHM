import java.util.LinkedList;
import java.util.Queue;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        Queue<Integer> queue = new LinkedList<>();

        for (int i = 1; i <= N; i++){
            queue.offer(i);
        }

        while(queue.size() > 1){
            queue.poll();
            int num = queue.poll();
            queue.offer(num);
        }

        System.out.println(queue.peek());
    }
}
