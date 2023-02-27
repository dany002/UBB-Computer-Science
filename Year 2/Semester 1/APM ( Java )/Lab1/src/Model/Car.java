package Model;

public class Car implements Vehicle{
    private int cost;
    private final String TYPE = "car";

    public Car() {
        this.cost = 0;
    }

    public Car(int new_cost){
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
        return "Car \t cost:\t" + this.cost;
    }
}
