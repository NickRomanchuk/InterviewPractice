public class ReverseArray{

    int[] reverse(int[] array){

        int[] new_array = new int[array.length];

        for (int i = 0; i < array.length; i++){
            new_array[i] = array[array.length - 1 - i];
        }

        return new_array;
    }

    public static void main(String[] args){
        ReverseArray example = new ReverseArray();
        int[] x = {1, 2, 3, 4, 5, 6};
        System.out.println(example.reverse(x)[0]);
    }
}