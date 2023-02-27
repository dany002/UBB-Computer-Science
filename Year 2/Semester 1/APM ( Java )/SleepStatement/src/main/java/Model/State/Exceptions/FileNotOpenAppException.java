package Model.State.Exceptions;

import Model.Exception.AppException;

public class FileNotOpenAppException extends AppException {
    public FileNotOpenAppException(String message){
        super(message);
    }
}
