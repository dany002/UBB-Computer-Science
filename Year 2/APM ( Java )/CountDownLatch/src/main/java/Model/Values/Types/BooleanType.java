package Model.Values.Types;

import Model.Exception.AppException;
import Model.Values.BooleanValue;
import Model.Values.Exceptions.InvalidOperationAppException;
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

    @Override
    public IType compose(String operation) throws AppException {
        switch(operation){
            case "and": return new BooleanType();
            case "or": return new BooleanType();
            case "==": return new BooleanType();
            case "!=": return new BooleanType();
            case "!": return new BooleanType();
        }
        throw new InvalidOperationAppException("InvalidOperationAppException: Cannot compose two BooleanValue types using operation " + operation);
    }
}
