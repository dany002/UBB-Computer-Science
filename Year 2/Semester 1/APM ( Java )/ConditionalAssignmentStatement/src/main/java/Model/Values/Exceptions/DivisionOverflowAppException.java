package Model.Values.Exceptions;

import Model.Exception.AppException;

public class DivisionOverflowAppException extends AppException {
    public DivisionOverflowAppException(String message){
        super(message);
    }
}
