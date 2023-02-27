package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.BinaryExpression;
import Model.Expressions.ConstantExpression;
import Model.Expressions.IExpression;
import Model.Expressions.VariableExpression;
import Model.State.ProgState;
import Model.Values.BooleanValue;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;


public class ForStatement implements IStatement{

    IStatement assignment;
    IExpression condition;
    IStatement step;
    IStatement statement;

    public ForStatement(IStatement assignment, IExpression condition, IStatement step, IStatement statement){
        this.assignment = assignment;
        this.condition = condition;
        this.step = step;
        this.statement = statement;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        progState.getExecutionStack().push(new WhileStatement(this.condition,new CompositeStatement(this.statement, this.step)));
        progState.getExecutionStack().push(this.assignment);
        return null;
    }

    @Override
    public String toString(){
        return "For( " + this.assignment.toString() + "; " + this.condition.toString() + "; " + this.step.toString() + "){ " + this.statement.toString() + "};";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if(!(new BooleanType()).equals(this.condition.typeCheck(typeEnv)))
            throw new AppException("For condition should evaluate to a BooleanType");
        this.assignment.typeCheck(typeEnv.copy());
        this.step.typeCheck(typeEnv.copy());
        this.statement.typeCheck(typeEnv.copy());
        return typeEnv;
    }
}

