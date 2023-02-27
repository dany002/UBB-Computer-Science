package Model.Expressions;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.BooleanValue;
import Model.Values.IValue;
import Model.Values.Types.IType;

public class UnaryExpression implements IExpression{
    IExpression expression;

    String operator;

    public UnaryExpression(IExpression expression, String operator){
        this.expression = expression;
        this.operator = operator;
    }

    @Override
    public IValue evaluate(ProgState state) throws AppException {
        return this.expression.evaluate(state).compose(new BooleanValue(),this.operator);
    }

    @Override
    public IType typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        IType type = this.expression.typeCheck(typeEnv);
        if(type == null)
            return null;
        return type.compose(this.operator);
    }

    @Override
    public String toString(){
        return "(" + this.operator + this.expression.toString() + ")";
    }
}
