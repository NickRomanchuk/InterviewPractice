public class InsertSort{

    int[] insertSort(int[] array){

        for (int i = 1; i < array.length; i++){

            int n = i;
            while ((n > 0) && (array[n - 1] > array[n])){
                
                int temp = array[n - 1];
                array[n - 1] = array[n];
                array[n] = temp;

                n -= 1;
            }
        }

        return array;
    }
    

    public static void main(String[] args){
        InsertSort example = new InsertSort();
        int[] x = {6, 5, 1, 2, 3, 8, 7};
        System.out.println(example.insertSort(x)[0]);
        System.out.println(example.insertSort(x)[1]);
        System.out.println(example.insertSort(x)[2]);
        System.out.println(example.insertSort(x)[5]);
        System.out.println(example.insertSort(x)[6]);
    }
}