
import java.util.Scanner;
public class Main {

    public static int factorials(int n){
        int p = 0;
        if (n==1){
            p=1;
        }else {
            p= factorials(n-1)*n;
        }
        return n;

    }
    public static void main(String[] args) {


        // int score = 10;

        // System.out.println(score);

        // score =100;
        // System.out.println(score);

        // score = score + 5;

        // System.out.println(score);

        // int a = 10;
        // int b = 3;

        // System.out.println(a + b);   // 13 (បូក)
        // System.out.println(a - b);   // 7  (ដក)
        // System.out.println(a * b);   // 30 (គុណ)
        // System.out.println(a / b);   // 3  (ចែក)
        // System.out.println(a % b);   // 1  (សល់ពីការចែក)

        // long even = 1, odd = 1, all = 1;
        // System.out.println("Enter N");
        // Scanner obj = new Scanner(System.in);
        // int a = obj.nextInt();

        // for (int i = 1; i <= a; i += 2) {
        //     odd *= i;
        // }

        // for (int i = 2; i <= a; i += 2) {
        //     even *= i;
        // }

        // for (int i = 1; i <= a; i++) {
        //     all *= i;
        // }

        // System.out.println("Even : " + even);
        // System.out.println("Odd : " + odd);
        // System.out.println("All  (N!): " + all);


        

    }
}