package Model.Expressions;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.RefValue;
import Model.Values.Types.IType;
import Model.Values.Types.RefType;

import java.sql.Ref;

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

    @Override
    public IType typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        IType type = this.expression.typeCheck(typeEnv);
        if(type instanceof RefType){
            RefType reft = (RefType) type;
            return reft.getInner();
        }
        else
            throw new AppException("The ReadHeap argument is not a RefType.");
    }
}
