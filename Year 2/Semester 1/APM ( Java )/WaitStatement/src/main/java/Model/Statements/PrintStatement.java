package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.Types.IType;

public class PrintStatement implements IStatement{
    IExpression expression;

    public PrintStatement(IExpression expression){
        this.expression = expression;
    }

    @Override
    public ProgState execute(ProgState state) throws AppException{
        state.getOutput().appendToOutput(this.expression.evaluate(state).toString());
        return null;
    }

    @Override
    public String toString(){
        return "print(" + this.expression.toString() + ")";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        this.expression.typeCheck(typeEnv);
        return typeEnv;
    }
}
