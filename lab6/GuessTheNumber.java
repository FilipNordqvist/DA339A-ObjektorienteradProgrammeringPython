import java.util.Scanner;
import java.util.Random;

public class GuessTheNumber{
  public static void main(String[] args) {
    /*Först lite kod för att vi ska kunna generera slumptal.
     Du behvöer inte bry dig inte om den första kodraden nedan riktigt än -
     vi kommer till detta i senare del av kursen.

     Slumptalen som fås på det här sättet är inte riktigt sanna slumptal
     utan går att förutsäga med viss kunskap om den bakomliggande koden.
     Så det här slumptalen är inte bra om vi ska kryptera något men duger gott
     för den här övningen eller något som inte är känsligt.
     */
    Random randomGenerator = new Random();
    int randomNumber;
    /*Kopiera kodraden nedan när du behöver ett nytt slumptal mellan 0-9.
    Du kan ändra intervallet genom att ändra värdet i parentesen.
    Det minsta slumtalet är 0 och det största du kan få är 1 mindre än
    det som ståd i parentesen. Så 10 i parentesen ger sluptal mellan 0-9,
    30 i parentesen ger slumptal mellan 0-29.
    */
    randomNumber = randomGenerator.nextInt(10);

    System.out.println("Visar första slumptalet vi fick: "+randomNumber); //kan raderas när du testat

    randomNumber = randomGenerator.nextInt(10); //okej - ett nytt slumptal, kan raderas när du testat
    System.out.println("Visar andra slumptalet vi fick: "+randomNumber); //kan raderas när du testat

   //här skriver du koden för ditt program,
  }
}
