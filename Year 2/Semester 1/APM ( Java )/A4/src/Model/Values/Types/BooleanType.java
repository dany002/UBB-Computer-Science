package Model.Values.Types;

import Model.Values.BooleanValue;
import Model.Values.IValue;

public class BooleanType implements IType{

    public BooleanType(){}

    @Override
    public IValue getDefaultValue() {
        return new BooleanValue(false);
    }

    @Override
    public String toString(){
        return "BooleanType";
    }

    @Override
    public boolean equals(IType other){
        return (other instanceof BooleanType);
    }
}
