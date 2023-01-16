import java.util.Scanner;

public class DominoPiling {

	public static void main(String[] args) {

		Scanner sc  = new Scanner(System.in);
		int n  = sc.nextInt();
		int m = sc.nextInt();
		int ans = m*n/2;
		System.out.println(ans);
	}
}
