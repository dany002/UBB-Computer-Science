package Model.Expressions;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Statements.IStatement;
import Model.Values.IValue;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;

public class MulExpression implements IExpression {

    IExpression expression1;
    IExpression expression2;

    public MulExpression(IExpression exp1, IExpression exp2) {
        this.expression1 = exp1;
        this.expression2 = exp2;
    }


    @Override
    public IValue evaluate(ProgState state) throws AppException {
        IValue first_value = this.expression1.evaluate(state);
        IValue second_value = this.expression2.evaluate(state);
        if (!(first_value.getType() instanceof IntegerType))
            throw new AppException("The first argument of MUL expression is not an integer.");
        if (!(second_value.getType() instanceof IntegerType))
            throw new AppException("The second argument of MUL expression is not an integer.");
        return new BinaryExpression(new ConstantExpression(new BinaryExpression(new ConstantExpression(first_value), new ConstantExpression(second_value), "*").evaluate(state)), new ConstantExpression(new BinaryExpression(new ConstantExpression(first_value), new ConstantExpression(second_value), "+").evaluate(state)), "-").evaluate(state);

    }

    @Override
    public String toString() {
        return "MUL( " + this.expression1.toString() + "," + this.expression2.toString() + ")";
    }

    @Override
    public IType typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        return null;
    }

}
