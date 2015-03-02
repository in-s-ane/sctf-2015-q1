import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Arrays;
import java.util.Scanner;

class Problem implements Comparable<Problem>{
    int p, d, t;
    public Problem(int p, int d, int t) {
        this.p = p;
        this.d = d;
        this.t = t;
    }
    
    int pointsLeft(int t1) {
        return p - d*(t+t1);
    }
    
    double ratio() {
        return ((double)t)/((double)d);
    }
    
    public String toString() {
        return ""+p+' '+d+' '+t;
    }

    @Override
    public int compareTo(Problem o) {
        return new Integer(t*o.d).compareTo(o.t*d);
    }
}

public class not_our_solution_for_degrees_kelvin {
    
    // N is total number of problems
    // T is bigger than the maximum time any problem can last 
    static int N, T = 40000;
    
    static Problem[] a;
    
    // arrays to store values for dynamic programming
    static int[] dp = new int[T];
    static int[] dp2 = new int[T];
    
    @SuppressWarnings("resource")
    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new FileReader("keelvin.txt"));
        N = s.nextInt();
        a = new Problem[N+1];
        for(int i = 1; i <= N; i++)
            a[i] = new Problem(s.nextInt(),s.nextInt(),s.nextInt());

        // add a place holder for problem at position 0
        a[0] = new Problem(0, 1, 0);
        
        // sorted based on t/d
        Arrays.sort(a);
        
        for(int t = 0; t < T; t++) {
                dp[t] = 0;
                dp2[t] = 0;
        }
        for(int i = a.length-1; i >= 1; i--) {
            
            // update dp values
            for(int t = T-1; t >= 0; t--)
                if(a[i].pointsLeft(t) > 0)
                    dp2[t] = Math.max(dp[t], dp[t+a[i].t]+a[i].pointsLeft(t));
            
            // shift new dp values back to first array
            for(int t = 0; t < T; t++)
                dp[t] = dp2[t];
        }
        System.out.println(dp[0]);
    }
}
