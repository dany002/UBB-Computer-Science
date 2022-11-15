package Model.Values.Exceptions;

import Model.Exception.AppException;

public class InvalidOperationAppException extends AppException {
    public InvalidOperationAppException(String message){
        super(message);
    }
}
