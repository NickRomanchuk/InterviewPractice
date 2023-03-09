public class Palidrome{

    public String Reverse(String S1){

        String new_string = "";
        for (int i = 0; i < S1.length(); i++){
            new_string = S1.charAt(i) + new_string;
        } 

        return new_string;
    }

    public Boolean isPalidrome(String S1){

        Boolean x = false;

        String reversed_string = this.Reverse(S1);

        if (S1.equals(reversed_string)){
            x = true;
            return x;
        }

        return x;
    }

    public static void main(String[] args){
        Palidrome example = new Palidrome();
        System.out.println(example.isPalidrome("Hello"));
        System.out.println(example.isPalidrome("HeleH"));
    }
}