public class Swap{

    int[] swapInts(int a, int b){

        int[] new_array = new int[2];

        b = a + b;
        a = b - a;
        b = b - a;

        new_array[0] = a;
        new_array[1] = b;

        return new_array;
    }

    public static void main(String[] args){

        Swap example = new Swap();
        System.out.println(example.swapInts(4, 8)[0]);
    }
}