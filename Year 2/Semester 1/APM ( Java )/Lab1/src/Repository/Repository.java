package Repository;

import Model.Vehicle;
import Exception.RepositoryFull;
import Exception.VehicleNotFound;
public class Repository implements RepoInterface{
    private Vehicle[] vehicles;
    private int index;

    private final int capacity = 100;

    public Repository(){
        this.vehicles = new Vehicle[capacity];
        this.index = 0;
    }

    @Override
    public void add(Vehicle a){
        if(this.index >= this.capacity)
            throw new RepositoryFull();
        else
            this.vehicles[this.index++] = a;
    }

    @Override
    public void remove(Vehicle a){
        int j = -1;
        for(int i = 0; i < index; i++)
            if(a.getCost() == this.vehicles[i].getCost() && a.getType().equals(this.vehicles[i].getType())) {
                j = i;
                break;
            }
        if(j == -1)
            throw new VehicleNotFound();
        for(int i = j; i < index - 1; i++)
            this.vehicles[i] = this.vehicles[i+1];
        this.index--;
    }

    @Override
    public Vehicle[] getAll(){
        return this.vehicles;
    }

    @Override
    public int getSize(){
        return this.index;
    }
}
