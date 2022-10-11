package Model;

public class Motorcycle implements Vehicle{
    private int cost;
    private final String TYPE = "motorcycle";

    public Motorcycle(){
        this.cost = 0;
    }

    public Motorcycle(int new_cost){
        this.cost = new_cost;
    }

    @Override
    public String getType(){
        return this.TYPE;
    }

    @Override
    public int getCost(){
        return this.cost;
    }

    @Override
    public String toString(){
        return "Motorcycle \t cost:\t" + this.cost;
    }
}
