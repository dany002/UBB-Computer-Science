package Model.Expressions;

import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.IValue;

public class VariableExpression implements IExpression{
    String name;

    public VariableExpression(String new_name){
        this.name = new_name;
    }

    @Override
    public IValue evaluate(ProgState state) throws AppException{
        return state.getSymTable().getValue(this.name);
    }

    @Override
    public String toString(){
        return this.name;
    }
}
