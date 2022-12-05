package Model.Expressions;

import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.RefValue;
import Model.Values.Types.RefType;

public class ReadHeapExpression implements IExpression{

    IExpression expression;

    public ReadHeapExpression(IExpression expr){
        this.expression = expr;
    }

    @Override
    public IValue evaluate(ProgState state) throws AppException {
        IValue value = this.expression.evaluate(state);
        if(!(value.getType() instanceof RefType))
            throw new AppException("Heap should only be accessed through references.");
        return state.getHeap().read(((RefValue) value).getAddress());
    }

    @Override
    public String toString(){
        return "readHeap(" + this.expression.toString() + ")";
    }
}
