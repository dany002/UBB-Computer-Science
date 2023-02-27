package Model.Expressions;

import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.IValue;

public class BinaryExpression implements IExpression{
    IExpression left;
    IExpression right;
    String operator;

    public BinaryExpression(IExpression left, IExpression right, String operator) {
        this.left = left;
        this.right = right;
        this.operator = operator;
    }

    @Override
    public IValue evaluate(ProgState state) throws AppException{
        return this.left.evaluate(state).compose(this.right.evaluate(state),this.operator);
    }

    @Override
    public String toString(){
        return "(" + this.left.toString() + " " + this.operator + " " + this.right.toString() + ")";
    }
}
