public class Bubble{

    int[] bubbleSort(int[] array){

        for (int i = 0; i < (array.length - 1); i++){

            for (int j = 0; j < array.length - i - 1; j++){

                if (array[j] > array[j + 1]){
                    int x = array[j + 1];
                    array[j + 1] = array[j];
                    array[j] = x;
                }
            }
        }

        return array;
    }

    public static void main(String[] args){
        Bubble example = new Bubble();
        int[] n = {6, 5, 1, 2, 3, 8, 7};
        System.out.println(example.bubbleSort(n)[0]);
        System.out.println(example.bubbleSort(n)[1]);
        System.out.println(example.bubbleSort(n)[5]);
        System.out.println(example.bubbleSort(n)[6]);
    }

}