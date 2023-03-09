public class Sum{

    int sumArray(int[] ints){

        int count = 0;

        for (int i = 0; i<ints.length; i++){
            count += ints[i];
        }

        return count;
    }

    public static void main(String[] args){
        Sum example = new Sum();
        int[] x = {1, 2, 3, 4, 5, 6};
        System.out.println(example.sumArray(x));
    }
}