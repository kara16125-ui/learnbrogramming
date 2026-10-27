
import java.util.Scanner;
public class nnnnn {
    public static int factorials(int n) {
        int p = 0;
        if (n == 1) {
            p = 1;
        } else {
            p = factorials(n - 1) * n;
        }
        return p;
    }

    public static void main(String[] args) {

        Scanner obj = new Scanner(System.in);
        System.out.println("places input Number N!=");
        System.out.println("result N!=" + factorials(obj.nextInt()));
    }
}