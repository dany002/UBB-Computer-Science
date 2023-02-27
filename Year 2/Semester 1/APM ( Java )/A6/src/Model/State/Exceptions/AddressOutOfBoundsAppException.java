package Model.State.Exceptions;

import Model.Exception.AppException;

public class AddressOutOfBoundsAppException extends AppException {
    public AddressOutOfBoundsAppException(String message){
        super(message);
    }
}
