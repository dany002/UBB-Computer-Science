package Model.Expressions;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.Types.IType;

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

    @Override
    public IType typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        return typeEnv.LookUp(this.name);
    }
}
