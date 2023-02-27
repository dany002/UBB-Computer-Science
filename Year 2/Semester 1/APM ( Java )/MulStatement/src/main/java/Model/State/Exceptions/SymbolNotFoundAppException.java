package Model.State.Exceptions;

import Model.Exception.AppException;

public class SymbolNotFoundAppException extends AppException {
    public SymbolNotFoundAppException(String message){
        super(message);
    }
}
