import java.io.*;
import java.util.*;

public class Main {

    static boolean[][] graph;
    static boolean[] visited;
    static int comCount, comMatchCount;
    static int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        comCount = Integer.parseInt(br.readLine());

        comMatchCount = Integer.parseInt(br.readLine());

        graph = new boolean[comCount + 1][comCount + 1];
        visited = new boolean[comCount + 1];

        for(int i = 0; i < comMatchCount; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a][b] = true;
            graph[b][a] = true;
        }

        dfs(1);

        System.out.println(count - 1);

    }

    public static void dfs(int start){
        visited[start] = true;
        count ++;

        for(int i = 1; i <= comCount; i++){
            if(graph[start][i] && !visited[i]){
                dfs(i);
            }
        }
    }
}
