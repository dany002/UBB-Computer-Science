package Model.State.Exceptions;

import Model.Exception.AppException;

public class InvalidFileFormatAppException extends AppException {
    public InvalidFileFormatAppException(String message){
        super(message);
    }
}
