//imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;
//import for Scanner and other utility classes
import java.util.*;
// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

class TestClass {

  public static int tallestBillboard(int[] rods) {
    int sum = 0;
    for (int rod : rods) {
      sum += rod;
    }

    int[] dp = new int[sum + 1];
    Arrays.fill(dp, -1);
    dp[0] = 0;

    for (int rod : rods) {
      int[] current = dp.clone();
      for (int i = 0; i <= sum - rod; i++) {
        if (current[i] < 0) continue;
        dp[i + rod] = Math.max(dp[i + rod], current[i]);
        dp[Math.abs(i - rod)] = Math.max(dp[Math.abs(i - rod)], 
            current[i] + Math.min(i, rod));
      }
    }
    return dp[0];
  }

  public static void main(String args[]) throws Exception {
    int n;
    Scanner sc= new Scanner(System.in);
    n = sc.nextInt();
    int[] array = new int[n];
    for(int i =0 ;i<n;i++){
      array[i] = sc.nextInt();
    }
    System.out.println(tallestBillboard(array));
  }
}
