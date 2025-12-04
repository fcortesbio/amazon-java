public class StringsUseEqualMethod {
	public static void main(String[] args) {
		String fruit1 = "Banana";
		String fruit2 = "banana";
		String fruit3 = "Banana";

		boolean result1 = fruit1.equals(fruit2);
		boolean result2 = fruit1.equals(fruit3);

		System.out.println("Using equals() method: \"" + fruit1 + "\" is equal to \"" + fruit2 + "\": " + result1);
		System.out.println("Using equals() method \"" + fruit1 + "\" is equal to \"" + fruit3 + "\": " + result2);

	}
}
