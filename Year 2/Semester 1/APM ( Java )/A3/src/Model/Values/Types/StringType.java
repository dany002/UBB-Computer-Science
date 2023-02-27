package Model.Values.Types;

import Model.Values.IValue;
import Model.Values.StringValue;

public class StringType implements IType{
    public StringType(){}

    @Override
    public IValue getDefaultValue() {
        return new StringValue("");
    }

    @Override
    public String toString(){
        return "StringType";
    }

}
