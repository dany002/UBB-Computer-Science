package Model.State.Exceptions;

import Model.Exception.AppException;

public class SymbolAlreadyExistsAppException extends AppException {
    public SymbolAlreadyExistsAppException(String message){
        super(message);
    }
}
