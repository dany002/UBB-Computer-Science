package Model.Expressions;

import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.IValue;

public interface IExpression {
    public IValue evaluate(ProgState state) throws AppException;
    public String toString();
}
