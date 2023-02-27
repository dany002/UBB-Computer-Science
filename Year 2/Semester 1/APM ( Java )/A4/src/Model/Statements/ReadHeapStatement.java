package Model.Statements;

import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;

public class ReadHeapStatement implements IStatement{
    IExpression expr;

    public ReadHeapStatement(IExpression expression){
        this.expr = expression;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        this.expr.evaluate(progState);
        return null;
    }

    @Override
    public String toString(){
        return this.expr.toString();
    }
}
