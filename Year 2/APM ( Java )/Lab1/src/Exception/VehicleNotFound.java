package Exception;

public class VehicleNotFound extends RuntimeException{
    public VehicleNotFound(){
        super("The vehicle is not found.");
    }

    public VehicleNotFound(String message){
        super(message);
    }
}
