public class FavoriteBook {

    // declaring empty attribues
    String bookTitle;
    String author;
    int pages;
    double price;

    // creating a constructor method
    public FavoriteBook(String bookTitle, String author, int pages, double price){
	this.bookTitle = bookTitle; 
	this.author = author; 
	this.pages = pages;
	this.price = price;
    }

    // creating an instance method to print book details
    public void printBookDetails(){
	System.out.println("Let me share some details about my favorite book...");
	System.out.println("Book title: " + this.bookTitle);
	System.out.println("Author: " + this.author);
	System.out.println("Number of pages: " + this.pages);
	System.out.println("Book price: COP $" + this.price);
    }
    public static void main(String[] args) {
        // creating an instance of the FavoriteBook
	FavoriteBook myBook = new FavoriteBook(
		"Niñapararoglaciar", 
		"Mariana Matija", 
		190, 
		102128.40
	);
        // executing the instance method;
	myBook.printBookDetails();
    }

}
