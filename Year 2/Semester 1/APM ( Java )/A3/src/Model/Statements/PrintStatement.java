package Model.Statements;

import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;

public class PrintStatement implements IStatement{
    IExpression expression;

    public PrintStatement(IExpression expression){
        this.expression = expression;
    }

    @Override
    public void execute(ProgState state) throws AppException{
        state.getOutput().appendToOutput(this.expression.evaluate(state).toString());
    }

    @Override
    public String toString(){
        return "print(" + this.expression.toString() + ")";
    }
}