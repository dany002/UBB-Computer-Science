package Model.Values.Types;

import Model.Exception.AppException;
import Model.Values.Exceptions.InvalidOperationAppException;
import Model.Values.IValue;
import Model.Values.RefValue;


public class RefType implements IType{
    IType inner;

    public RefType(IType inner){
        this.inner = inner;
    }

    public IType getInner(){
        return this.inner;
    }

    @Override
    public IValue getDefaultValue(){
        return new RefValue(0, inner);
    }

    @Override
    public String toString() {
        return "RefType " + this.inner.toString();
    }

    @Override
    public boolean equals(IType other){
        return (other instanceof RefType) && ((RefType) other).inner != null && ((RefType) other).inner.equals(this.inner);
    }

    @Override
    public IType compose(String operation) throws AppException {
        throw new InvalidOperationAppException("InvalidOperationAppException: Cannot compose two RefValue types using operator " + operation);
    }
}
