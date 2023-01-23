package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.RefValue;
import Model.Values.Types.IType;
import Model.Values.Types.RefType;

import java.sql.Ref;

public class WriteHeapStatement implements IStatement{

    IExpression addressExpression;
    IExpression valueExpression;

    public WriteHeapStatement(IExpression addressExpression, IExpression valueExpression){
        this.addressExpression = addressExpression;
        this.valueExpression = valueExpression;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue address = this.addressExpression.evaluate(progState);
        IValue value = this.valueExpression.evaluate(progState);
        if(!(address.getType() instanceof RefType))
            throw new AppException("Heap should be accessed only using references.");
        progState.getHeap().write(((RefValue)address).getAddress(), value);
        return null;
    }

    @Override
    public String toString(){
        return "WriteHeap(" + this.addressExpression.toString() + ", " + this.valueExpression.toString() + ")";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        IType addressType = this.addressExpression.typeCheck(typeEnv);
        this.valueExpression.typeCheck(typeEnv);
        if(!(addressType instanceof RefType))
            throw new AppException("Write heap expression doesn't evaluate to a RefType.");
        return typeEnv;
    }
}
