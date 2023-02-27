package Controller;

import Model.Car;
import Model.Motorcycle;
import Model.Truck;
import Model.Vehicle;
import Repository.Repository;
import Exception.VehicleError;


public class Controller {

    private Repository repo;

    public Controller(){
        this.repo = new Repository();
    }

    public Controller(Repository new_repo){
        this.repo = new_repo;
    }

    public void add(String vehicle_type, int cost){
        Vehicle new_vehicle;
        if(vehicle_type.equals("car")){
            new_vehicle = new Car(cost);
        }
        else if(vehicle_type.equals("truck")) {
            new_vehicle = new Truck(cost);
        }
        else if(vehicle_type.equals("motorcycle")){
            new_vehicle = new Motorcycle(cost);
        }
        else{
            throw new VehicleError();
        }
        this.repo.add(new_vehicle);
    }

    public void remove(String vehicle_type, int cost){
        Vehicle new_vehicle;
        if(vehicle_type.equals("car")){
            new_vehicle = new Car(cost);
        }
        else if(vehicle_type.equals("truck")) {
            new_vehicle = new Truck(cost);
        }
        else if(vehicle_type.equals("motorcycle")){
            new_vehicle = new Motorcycle(cost);
        }
        else{
            throw new VehicleError();
        }
        this.repo.remove(new_vehicle);
    }

    public Vehicle[] getAll(){
        return this.repo.getAll();
    }

    public int getSize(){
        return this.repo.getSize();
    }

}
