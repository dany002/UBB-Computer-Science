package Model.Statements;

import Model.Exception.AppException;
import Model.State.ProgState;

public class NoOperationStatement implements IStatement{
    public NoOperationStatement(){

    }

    @Override
    public void execute(ProgState state) throws AppException{

    }

    @Override
    public String toString(){
        return "NOP";
    }
}
