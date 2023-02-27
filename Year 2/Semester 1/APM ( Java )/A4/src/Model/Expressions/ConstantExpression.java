package Model.Expressions;

import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.IValue;

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
}
