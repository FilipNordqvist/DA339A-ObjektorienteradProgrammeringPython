

"""
import java.util.Scanner;
 * @author Amir Parmbäck
 * @version 1.0
 * Created 010920
 * This class represents a small program that asks the user for his or her name
 * and prints it out. The input to the program is given in the console through Scanner.
 */

"""

#En funktion som tar emot ett namn är skriver ut det.
def Lab2Exercise2():
    name = input("Hej, ange ditt namn! ")
    print(f"Ditt namn är {name}")

Lab2Exercise2()



"""
public class Lab2Exercise2 {
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Hej, ange ditt namn!");
        String name = scanner.nextLine();
        System.out.println("Ditt namn är " + name);
    }
}
"""
