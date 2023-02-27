package Model;

public class Truck implements Vehicle{
    private int cost;
    private final String TYPE = "truck";

    public Truck(){
        this.cost = 0;
    }

    public Truck(int new_cost){
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
        return "Truck \t cost:\t" + this.cost;
    }
}
