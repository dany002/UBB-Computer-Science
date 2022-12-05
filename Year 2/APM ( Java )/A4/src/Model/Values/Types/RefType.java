package Model.Values.Types;

import Model.Values.IValue;
import Model.Values.RefValue;


public class RefType implements IType{
    IType inner;

    public RefType(IType inner){
        this.inner = inner;
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
}
