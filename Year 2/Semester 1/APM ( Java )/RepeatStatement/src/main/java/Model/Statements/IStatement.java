package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.Types.IType;

public interface IStatement {
    public ProgState execute(ProgState progState) throws AppException;
    public String toString();

    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String,IType> typeEnv) throws AppException;
}
