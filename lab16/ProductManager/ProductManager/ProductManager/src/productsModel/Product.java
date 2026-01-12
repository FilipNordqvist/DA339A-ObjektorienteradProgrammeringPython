package productsModel;


public class Product
{
    private String name;
    private double price;  //utan moms
    private int count; //antalet av denna product

    private ProductType productType;
    private UnitType unit;


    public Product()
    {
        initializeValues();
    }
    public void initializeValues()
    {
        name = "No name";
        productType = ProductType.Food;


        unit = UnitType.kg;
    }
    public Product (String name, double price)
    {
        this.name = name;
        this.price = price;
        initializeValues();
    }


    public String getName()
    {
        return name;
    }
    //setter --> input
    public void setName(String name)
    {
        if ((name != null) && (name !=""))
           this.name = name;
    }

    public double calcTotalPrice()
    {
        double vat = calcVAT();
        double totalPrice = price + vat;
        return totalPrice;
    }

    public double calcVAT()
    {
        double amount = VATCalculator.getVATFactor(productType) * price;
        return amount;
    }


    //getter och setter
    public double getPrice()
    {
        return price;
    }

    public void setPrice(double price)
    {
        this.price = price;
    }

    public int getCount()
    {
        return count;
    }

    public void setCount(int count)
    {
        this.count = count;
    }


    public ProductType getProductType()
    {
        return productType;
    }

    public void setProductType(ProductType productType)
    {
        this.productType = productType;
    }

    public UnitType getUnit()
    {
        return unit;
    }

    public void setUnit(UnitType unit)
    {
        this.unit = unit;
    }


    public String toString()
    {
        double vat = calcVAT();
        String strInfo =
                String.format("Name %16s\nPrice %15.2f\nCount %15d\nUnit %16s\nCategory %13s\n\nVat (moms) %8.2f",
                         name, price, count,unit.name(),  productType.name(),vat);

        return strInfo;


    }
}
