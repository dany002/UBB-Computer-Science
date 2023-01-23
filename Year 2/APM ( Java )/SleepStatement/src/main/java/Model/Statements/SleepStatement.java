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
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;

public class SleepStatement implements IStatement{

    IExpression expression;

    public SleepStatement(IExpression expression){
        this.expression = expression;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue value = this.expression.evaluate(progState);
        if(!(value.getType() instanceof IntegerType))
            throw new AppException("The argument of sleep statement has to be a number.");
        IValue new_value = new BinaryExpression(new ConstantExpression(value), new ConstantExpression(new IntegerValue(1)),"-").evaluate(progState);
        IValue test_negative = new BinaryExpression(new ConstantExpression(value), new ConstantExpression(new IntegerValue(0)),"<").evaluate(progState);
        if(test_negative.equals(new BooleanValue(true)))
            throw new AppException("The argument of sleep statement is less than 0.");
        if(!value.equals(new IntegerValue(0)))
            progState.getExecutionStack().push(new SleepStatement(new ConstantExpression(new_value)));
        return null;
    }

    @Override
    public String toString(){
        return "sleep(" + this.expression.toString() + ");";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if(!(new IntegerType()).equals(this.expression.typeCheck(typeEnv)))
            throw new AppException("The argument of sleep statement has to be a number.");
        return typeEnv;
    }
}
