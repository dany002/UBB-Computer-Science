package Model.Values.Types;

import Model.Exception.AppException;
import Model.Values.Exceptions.InvalidOperationAppException;
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

    @Override
    public boolean equals(IType other){
        return (other instanceof IntegerType);
    }

    @Override
    public IType compose(String operation) throws AppException {
        switch (operation){
            case "+": return new IntegerType();
            case "-": return new IntegerType();
            case "*": return new IntegerType();
            case "/": return new IntegerType();
            case "<": return new BooleanType();
            case "<=": return new BooleanType();
            case ">": return new BooleanType();
            case ">=": return new BooleanType();
            case "==": return new BooleanType();
            case "!=": return new BooleanType();
        }
        throw new InvalidOperationAppException("InvalidOperationAppException: Cannot compose two IntegerValue types using operator " + operation);
    }
}
