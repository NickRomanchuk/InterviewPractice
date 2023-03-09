public class Reverse{

    public String reversed(String s1){

        String new_string = "";
        for (int i = 0; i < s1.length(); i++){
            new_string = s1.charAt(i) + new_string;
        }
        
        return new_string;
    }

    public static void main(String[] args){
        Reverse x = new Reverse();
        System.out.println(x.reversed("Hello"));

    }
}