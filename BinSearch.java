public class BinSearch{

    int runSearch(int[] array, int n){

        int max = array.length;
        int min = 0;

        while (min <= max){

            int mid = (max + min) / 2;
            System.out.println(mid);
            System.out.println(max);
            System.out.println(min);
            System.out.println();

            if (array[mid] < n){
                min = mid + 1;
            }
            else if (array[mid] > n){
                max = mid - 1;
            }
            else{
                return mid;
            }

        }

        return -1;
    }

    public static void main(String[] args){
        BinSearch example = new BinSearch();
        int[] x = {1, 2, 3, 4, 5, 6, 7, 8};
        System.out.println(example.runSearch(x, 4));
    }
}