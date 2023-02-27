package Model.Expressions;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.Types.IType;

public interface IExpression {
    public IValue evaluate(ProgState state) throws AppException;
    public String toString();

    public IType typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException;
}
