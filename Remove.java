public class Remove{

    String removeChar(String S1, Character c){

        String new_string = "";

        for (int i = 0; i < S1.length(); i++){
            if (S1.charAt(i) != c){
                new_string += S1.charAt(i);
            }
        }

        return new_string;
    }

    public static void main(String[] args){
        Remove example = new Remove();
        System.out.println(example.removeChar("hello", 'e'));
    }
}