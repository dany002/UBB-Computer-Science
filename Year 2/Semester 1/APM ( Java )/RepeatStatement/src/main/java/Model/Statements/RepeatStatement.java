package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.Expressions.UnaryExpression;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IType;

public class RepeatStatement implements IStatement{

    IStatement statement;
    IExpression expression;

    public RepeatStatement(IStatement statement, IExpression expression){
        this.statement = statement;
        this.expression = expression;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue value = this.expression.evaluate(progState);
        if(!(value.getType() instanceof BooleanType))
            throw new AppException("Invalid expression value in repeat until.");
        System.out.println("HI!");
        progState.getExecutionStack().push(new CompositeStatement(this.statement, new WhileStatement(new UnaryExpression(this.expression,"!"), this.statement)));
        return null;
    }

    @Override
    public String toString(){
        return "(repeat (" + this.statement.toString() + ") until " + this.expression.toString() + ")";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if((new BooleanType()).equals(this.expression.typeCheck(typeEnv)))
            return this.statement.typeCheck(typeEnv);
        throw new AppException("While condition doesn't evaluate to a BooleanType.");
    }
}
