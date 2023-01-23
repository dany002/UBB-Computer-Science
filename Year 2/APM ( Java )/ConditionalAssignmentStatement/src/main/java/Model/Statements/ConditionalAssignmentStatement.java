package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.ConstantExpression;
import Model.Expressions.IExpression;
import Model.Expressions.VariableExpression;
import Model.State.ProgState;
import Model.Values.BooleanValue;
import Model.Values.IValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IType;

public class ConditionalAssignmentStatement implements IStatement{

    String variable;
    IExpression exp1;
    IExpression exp2;
    IExpression exp3;

    public ConditionalAssignmentStatement(String variable, IExpression exp1, IExpression exp2, IExpression exp3){
        this.variable = variable;
        this.exp1 = exp1;
        this.exp2 = exp2;
        this.exp3 = exp3;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue value = this.exp1.evaluate(progState);
        if(!(value.getType() instanceof BooleanType))
            throw new AppException("Invalid expression value for conditional assignment statement.");
        progState.getExecutionStack().push(new IfStatement(this.exp1, new AssignmentStatement(this.variable, new ConstantExpression(this.exp2.evaluate(progState))),new AssignmentStatement(this.variable, new ConstantExpression(this.exp3.evaluate(progState)))));
        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {

        if(!(new BooleanType()).equals(this.exp1.typeCheck(typeEnv)))
            throw new AppException("Invalid expression value for conditional assignment statement.");
        return typeEnv;
    }

    @Override
    public String toString(){
        return this.variable + " = " + this.exp1.toString() + "?" + this.exp2.toString() + ":" + this.exp3.toString();
    }
}
