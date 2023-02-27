package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.BooleanValue;
import Model.Values.IValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IType;

public class IfStatement implements  IStatement{
    IExpression expression;
    IStatement left;
    IStatement right;

    public IfStatement(IExpression expression, IStatement left, IStatement right){
        this.expression = expression;
        this.left = left;
        this.right = right;
    }

    @Override
    public ProgState execute(ProgState state) throws AppException{
        IValue value = this.expression.evaluate(state);
        if(!(value.getType() instanceof BooleanType))
            throw new AppException("Invalid expression value for if statement.");
        if(((BooleanValue) value).getValue())
            state.getExecutionStack().push(this.left);
        else
            state.getExecutionStack().push(this.right);
        return null;
    }

    @Override
    public String toString(){
        return "if(" + this.expression.toString() + ")then { " + this.left.toString() + "} else {" + this.right.toString() + "}";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        IType typexp = this.expression.typeCheck(typeEnv);
        if(!(new BooleanType()).equals(this.expression.typeCheck(typeEnv)))
            throw new AppException("If condition doesn't evaluate to a BooleanType.");
        this.left.typeCheck(typeEnv.copy());
        this.right.typeCheck(typeEnv.copy());
        return typeEnv;

    }
}

