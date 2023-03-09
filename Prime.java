public class Prime{

    Boolean run(int n){

        if (n > 1) {
            for (int i = 2; i < (n / 2); i++){
                if (n % (i+1) == 0){
                    return false;
                }
            }

            return true;      
        }

        return false;
    }


    public static void main(String[] args){
        Prime example = new Prime();

        System.out.println(example.run(7));
    }
}