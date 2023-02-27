package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.BooleanValue;
import Model.Values.IValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IType;

public class WhileStatement implements IStatement{

    IExpression condition;
    IStatement statement;

    public WhileStatement(IExpression expression, IStatement statement){
        this.condition = expression;
        this.statement = statement;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue value = this.condition.evaluate(progState);
        if(!(value.getType() instanceof BooleanType))
            throw new AppException("While condition should evaluate to a BooleanType.");
        if(((BooleanValue) value).getValue()) {
            progState.getExecutionStack().push(this);
            progState.getExecutionStack().push(statement);
        }
        return null;
    }

    @Override
    public String toString(){
        return "While(" + this.condition.toString() + "){" + this.statement.toString() + "};";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if((new BooleanType()).equals(this.condition.typeCheck(typeEnv)))
            return this.statement.typeCheck(typeEnv);
        throw new AppException("While condition doesn't evaluate to a BooleanType.");
    }
}
