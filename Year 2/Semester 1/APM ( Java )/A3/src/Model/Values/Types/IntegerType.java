package Model.Values.Types;

import Model.Values.IValue;
import Model.Values.IntegerValue;

public class IntegerType implements IType{

    public IntegerType(){}

    @Override
    public IValue getDefaultValue(){
        return new IntegerValue(0);
    }

    @Override
    public String toString(){
        return "IntegerType";
    }
}
