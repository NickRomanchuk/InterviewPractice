public class Fibonacci{

    int run(int n){
        
        if (n == 1){
            return 0;
        }
        else if (n == 2){
            return 1;
        }
        else{
            return this.run(n - 1) + this.run(n - 2);
        }
    }

    public static void main(String[] args){
        Fibonacci example = new Fibonacci();
        System.out.println(example.run(8));
    }
}

