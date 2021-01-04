import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.ArrayList;  
public class Main {
 

    public static String getRecipient(String message, int position) {
        List<String> allMatches = new ArrayList<String>();
        Matcher m = Pattern.compile("your regular expression here").matcher(yourStringHere);
 
        while (m.find()) {
            allMatches.add(m.group());
        }
            
    }
    
}
