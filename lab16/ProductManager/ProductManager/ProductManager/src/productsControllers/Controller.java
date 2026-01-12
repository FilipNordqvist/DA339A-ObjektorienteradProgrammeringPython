package productsControllers;

import  productsView.*;
import productsModel.*;


public class Controller
{
    MainFrame view;
    Product product;  //model

    //constructor
    public Controller()
    {
        product = new Product();
        view = new MainFrame(this);
        updateView();
    }

    //Denna metod anropas varje gång någon ändring av modellen sker
    private void updateView()
    {
        view.showProductInfo(product.toString());

    }

    //Denna metod anropas av view
    public void buttonPressed(ButtonType button)
    {
        switch (button)
        {
            case Add:
            case Change:
                validateAndSaveProduct();
                break;

            case Delete:
                product = new Product();   //noll-ställ
                break;
        }
        updateView();
    }


    private void validateAndSaveProduct()
    {
        String name = view.getNameText();
        String strPrice = view.getPriceText();


        if ( (name != null)  && (!name.isEmpty()) )
            product.setName(name);
         else
            view.errMessage("Give a valid name");

          try
        {
            product.setPrice(Double.parseDouble(strPrice));


        }
        catch (NumberFormatException e)
        {
            view.errMessage("Invalid price or count!");
        }
    }
    public void setUnitItem(Object unit)
    {
        if (product != null)
            product.setUnit ((UnitType)unit);
    }
    public UnitType [] getUnitItems()
    {
        return UnitType.values ();
    }

}
