package Model.Statements;

import Model.Exception.AppException;
import Model.State.ProgState;

public class NoOperationStatement implements IStatement{
    public NoOperationStatement(){

    }

    @Override
    public ProgState execute(ProgState state) throws AppException{
        return null;
    }

    @Override
    public String toString(){
        return "NOP";
    }
}
