public class Cipher {
    public static void main(String[] args) {
        System.out.println(Cipher.halliday("Pelfgny Xrl"));
    }
    public static String halliday(String message){
        int shift = 13;
        String s = "";

 

        for (int i=0; i <message.length();i++){
            char originalC = (message.charAt(i));

 

            char decodedC = (char) (originalC+shift);
            
            if (Character.isUpperCase(originalC) && decodedC > 'Z' ||
                    Character.isLowerCase(originalC) && decodedC > 'z'){
                s += (char)(decodedC - 26);
            }
            else if (!Character.isAlphabetic(originalC)) s += originalC;
            else s += decodedC;

 

        }
        return s;
    }
}
