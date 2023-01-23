package Model.State.Exceptions;

import Model.Exception.AppException;

public class FileAlreadyOpenAppException extends AppException {
    public FileAlreadyOpenAppException(String message){
        super(message);
    }
}
