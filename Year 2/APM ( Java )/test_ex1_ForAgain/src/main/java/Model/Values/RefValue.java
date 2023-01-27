package Model.Values;

import Model.Exception.AppException;
import Model.Values.Types.IType;
import Model.Values.Types.RefType;

import java.sql.Ref;

public class RefValue implements IValue{
    int address;
    IType innerType;

    public RefValue(int address, IType innerType){
        this.address = address;
        this.innerType = innerType;
    }

    @Override
    public boolean equals(Object other){
        return (other instanceof RefValue) && ((RefValue) other).address == this.address && this.innerType.equals(((RefValue) other).innerType);
    }

    @Override
    public IValue compose(IValue other, String operation) {
        return null;
    }

    @Override
    public IType getType() {
        return new RefType(innerType);
    }

    @Override
    public boolean equals(IValue other) {
        return (other instanceof RefValue) && this.address == ((RefValue) other).address && this.getType().equals(other.getType());
    }

    @Override
    public IValue clone() {
        return new RefValue(this.address, this.innerType);
    }

    @Override
    public String toString(){
        return "Ref(" + Integer.toString(this.address) + "," + this.innerType.toString() + ")";
    }

    public int getAddress(){
        return this.address;
    }
}
