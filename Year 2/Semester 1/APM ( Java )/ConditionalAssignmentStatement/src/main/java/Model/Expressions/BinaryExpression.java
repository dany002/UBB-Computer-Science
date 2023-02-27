package Model.Expressions;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;

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

    @Override
    public IType typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        IType firstType = this.left.typeCheck(typeEnv);
        IType secondType = this.right.typeCheck(typeEnv);
        if(firstType == null || secondType == null){
            return null;
        }
        if(firstType == null || !firstType.equals(secondType)) {
            throw new AppException("Binary expression operands are not the same");
        }
        return firstType.compose(this.operator);
    }


}
