public class subStrings {
    public static void main(String[] args) {
        String fruit = "banana";
        fruit.length();

        String partFrom1to4 = fruit.substring(1, 4);
        String partFrom4to5 = fruit.substring(4, 5);

        System.out.println("The full string is: " + fruit);
        System.out.println("Substring from index 1 to 4, 4 excluded: " + partFrom1to4);
        System.out.println("Substring from indexx 4 to 5, 5 excluded: " + partFrom4to5);

    }

}