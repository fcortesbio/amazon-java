public class CurrencyConversion {
	public static void main(String[] args){
		// variable declaration
		double amountInUSD = 100.00;
		double exchangeRateUSDtoEUR = 0.85; // (1 USD = 0.85 EUE)
		double balance = amountInUSD;

		System.out.println("Initial USD amount: " + balance);
		// Performing curr conversion
		
		balance *= exchangeRateUSDtoEUR;
		System.out.println("Amount in EUR: " + balance);

		// deducting 55EUR as the stated expenditure and print the balance
		balance -= 55;
		System.out.println("After expenditure (EUR): " + balance);

		balance /= exchangeRateUSDtoEUR; // 1 USD = 1 / 0.85 EUR
		System.out.println("Final amount USD: " + balance); 
	}
}
