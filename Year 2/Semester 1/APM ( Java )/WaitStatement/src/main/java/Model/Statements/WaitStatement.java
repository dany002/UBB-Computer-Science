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

public class WaitStatement implements IStatement{

    IExpression expression;

    public WaitStatement(IExpression expression){
        this.expression = expression;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue value = this.expression.evaluate(progState);
        if(!(value.getType() instanceof IntegerType))
            throw new AppException("The argument of wait has to be a number.");
        IValue test_negative = new BinaryExpression(new ConstantExpression(value), new ConstantExpression(new IntegerValue(0)),"-").evaluate(progState);
        if(test_negative.equals(new BooleanValue(true)))
            throw new AppException("The argument of wait is less than 0.");
        IValue new_value = new BinaryExpression(new ConstantExpression(value), new ConstantExpression(new IntegerValue(1)),"-").evaluate(progState);
        if(!value.equals(new IntegerValue(0)))
            progState.getExecutionStack().push(new CompositeStatement(new PrintStatement(new ConstantExpression(value)),new WaitStatement(new ConstantExpression(new_value))));

        return null;
    }

    @Override
    public String toString(){
        return "wait(" + this.expression.toString() + ");";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if(!(new IntegerType()).equals(this.expression.typeCheck(typeEnv)))
            throw new AppException("The argument of wait has to be a number.");
        return typeEnv;
    }
}
