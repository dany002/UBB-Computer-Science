package Model.Statements;

import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;

public class AssignmentStatement implements IStatement{
    String variableName;
    IExpression expression;

    public AssignmentStatement(String variableName, IExpression expression){
        this.variableName = variableName;
        this.expression = expression;
    }

    @Override
    public ProgState execute(ProgState state) throws AppException{
        state.getSymTable().setValue(this.variableName, this.expression.evaluate(state));
        return null;
    }

    @Override
    public String toString(){
        return this.variableName + " = " + this.expression.toString();
    }
}
