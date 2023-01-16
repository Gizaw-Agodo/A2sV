import java.util.Arrays; 
public class Tutorialcup {
    public static int  maxCoins(int[] piles) {
          Arrays.sort(piles);
        int res = 0, n = piles.length;
        for (int i = n / 3; i < n; i += 2)
            res += piles[i];
        return res;
    }
  public static void main(String[] args) {
    int [] arr = {9,8,7,6,5,1,2,3,4}; 
    int ans=  maxCoins(arr);
    System.out.println(ans);
  }
}
