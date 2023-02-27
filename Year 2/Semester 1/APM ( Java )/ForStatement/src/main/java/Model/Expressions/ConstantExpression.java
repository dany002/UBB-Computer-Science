package Model.Expressions;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.Types.IType;

public class ConstantExpression implements IExpression{
    IValue value;

    public ConstantExpression(IValue new_value){
        this.value = new_value;
    }

    @Override
    public IValue evaluate(ProgState state) throws AppException{
        return this.value;
    }

    @Override
    public String toString(){
        return this.value.toString();
    }

    @Override
    public IType typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        return this.value.getType();
    }
}
