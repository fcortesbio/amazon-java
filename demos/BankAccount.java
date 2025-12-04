// example for OOP encapsulation principle
public class BankAccount {
	// Private field - Encapsulated
	private double balance;

	// Public constructor
	public BankAccount(double initialBalance) {
		this.balance = initialBalance;
	}

	// Public Getter method - Controlled read access
	public double getBalance(){
		return this.balance;
	}
	// Public Setter/Mutator method - Controlled write access (with validation)
	public void deposit(double amount) {
		if (amount > 0) {
			this.balance += amount;
		}
	}

	public static void main(String[] args){
		
	} 
}
