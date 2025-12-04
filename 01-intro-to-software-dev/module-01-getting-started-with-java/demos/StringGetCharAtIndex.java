public class StringGetCharAtIndex {
    public static void main(String[] args) {

        String fruit = "Banana";

        // This will be `a`, because `B` is at index 0 and `a` is at index 1
        for (int i = 0; i < fruit.length(); i++) {
            int index = i;
            char letter = fruit.charAt(index);
            System.out.println("The character at index " + index + " is: " + letter);
        }
    }
}