public class Factorial{

    int run(int n){

        int x = 1;

        if (n == 0){
            return 1;
        }
        else{
            for (int i = 1; i <= n; i++){
                x *= i;
            }

            return x;
        }
    }

    public static void main(String[] args){
        Factorial example = new Factorial();
        System.out.println(example.run(6));
    }
}