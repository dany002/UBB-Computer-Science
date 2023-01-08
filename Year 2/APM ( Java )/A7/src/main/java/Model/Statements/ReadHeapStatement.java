package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.Types.IType;

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

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        this.expr.typeCheck(typeEnv);
        return typeEnv;
    }
}
