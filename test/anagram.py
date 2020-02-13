#find if 2 strings are anagrams of each other
# Get the ASCII number of a character: >> number = ord(char)
# Get the character given by an ASCII number >> char = chr(number)
# See this link for how to do this with sorting: https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
'''
//Implementation in Java:
public class Anagram{
    public static void main(String [] args){
        System.out.println(anagram("fireds", "fried"));
    }
    
    public static boolean anagram(String first, String second){
        int count_f = 0;
        int count_s = 0;
        
        for (int i = 0; i<first.length(); i++){
            count_f += (int) first.charAt(i);
        }
        
        for (int j = 0; j<second.length(); j++){
            count_s += (int) second.charAt(j);
        }
        
        if (count_f == count_s) return true;
        else return false;
    }
}
'''
#Implementation in Python
def anag_check(first, second):
    count_f = 0
    count_s = 0
    for c in first:
        count_f += ord(c)
    for d in second:
        count_s += ord(d)
    if count_f == count_s:
        return True
    else:
        return False


print(anag_check('fied', 'fired'))
