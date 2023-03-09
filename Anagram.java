public class Anagram{
    public int count(String S1, Character c){

        int count = 0;

        for(int i = 0; i < S1.length(); i++){
            if(S1.charAt(i) == c){
                count += 1;
            }
        }

        return count;
    }

    public Boolean isAnagram(String S1, String S2){

        Boolean b = true;

        if (S1.length() != S1.length()){
            b = false;
            return b;
        }

        for (int i = 0; i < S1.length(); i++){
            int S1_count = this.count(S1, S1.charAt(i));
            int S2_count = this.count(S2, S2.charAt(i));

            if (S1_count != S2_count){
                b = false;
                return b;
            }
        }

        return b;
    }


    public static void main(String[] args){
        Anagram example = new Anagram();

        System.out.println(example.isAnagram("cinema", "iceean"));
    }
}