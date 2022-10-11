package Exception;

public class VehicleError extends RuntimeException{

    public VehicleError(){
        super("You have to choose between car, motorcycle or truck.");
    }

    public VehicleError(String message){
        super(message);
    }
}
