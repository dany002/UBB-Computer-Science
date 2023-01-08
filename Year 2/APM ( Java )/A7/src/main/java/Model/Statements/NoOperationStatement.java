package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.Types.IType;

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

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        return typeEnv;
    }
}
