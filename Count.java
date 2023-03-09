public class Count{

    public int countChar(String S1, Character c){

        int count = 0;

        for(int i = 0; i < S1.length(); i++){
            if(S1.charAt(i) == c){
                count += 1;
            }
        }

        return count;
    }

    public static void main(String[] args){
        Count example = new Count();

        System.out.println(example.countChar("Hello", 'i'));
    }
}