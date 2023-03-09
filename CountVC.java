public class CountVC{

    public int run(String S1){

        int v_count = 0;

        for (int i = 0; i < S1.length(); i++){
            Character x = S1.charAt(i);

            if (x == 'a' | x == 'e' | x == 'i' | x == 'o' | x == 'u'){
                v_count += 1;
            }
        }

        return v_count;
    }


    public static void main(String[] args){
        CountVC example = new CountVC();
        System.out.println(example.run("Hello"));
    }
}