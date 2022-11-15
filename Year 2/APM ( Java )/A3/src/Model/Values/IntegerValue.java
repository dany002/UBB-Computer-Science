package Model.Values;

import Model.Values.Exceptions.DivisionOverflowAppException;
import Model.Values.Exceptions.InvalidOperationAppException;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;

public class IntegerValue implements IValue {

    int value;

    public IntegerValue(){
        this.value = 0;
    }

    public IntegerValue(int new_value){
        this.value = new_value;
    }

    public IntegerValue add(IntegerValue other){
        return new IntegerValue(this.value + other.value);
    }

    public IntegerValue subtract(IntegerValue other){
        return new IntegerValue(this.value - other.value);
    }

    public IntegerValue multiply(IntegerValue other){
        return new IntegerValue(this.value * other.value);
    }

    public IntegerValue divide(IntegerValue other) throws DivisionOverflowAppException{
        if (other.value == 0)
            throw new DivisionOverflowAppException("DivisionOverflowAppException: Cannot divide by 0.");
        return new IntegerValue(this.value / other.value);
    }

    private BooleanValue lessThan(IntegerValue other){
        return new BooleanValue(this.value < other.value);
    }

    private BooleanValue lessThanEqual(IntegerValue other){
        return new BooleanValue(this.value <= other.value);
    }

    private BooleanValue greaterThan(IntegerValue other){
        return new BooleanValue(this.value > other.value);
    }

    private BooleanValue greaterThanEqual(IntegerValue other){
        return new BooleanValue(this.value >= other.value);
    }

    private BooleanValue equal(IntegerValue other){
        return new BooleanValue(this.equals(other));
    }

    private BooleanValue notEqual(IntegerValue other){
        return new BooleanValue(!this.equals(other));
    }


    @Override
    public String toString(){
        return Integer.toString(this.value);
    }

    @Override
    public IValue compose(IValue other, String operation) throws InvalidOperationAppException, DivisionOverflowAppException {
        if(!(other.getType() instanceof IntegerType))
            throw new InvalidOperationAppException("InvalidOperationAppException: Cannot compose two different types using operator " + operation);
        switch(operation){
            case "+": return this.add((IntegerValue) other);
            case "-": return this.subtract((IntegerValue) other);
            case "*": return this.multiply((IntegerValue) other);
            case "/": return this.divide((IntegerValue) other);
            case "<": return this.lessThan((IntegerValue) other);
            case "<=": return this.lessThanEqual((IntegerValue) other);
            case ">": return this.greaterThan((IntegerValue) other);
            case ">=": return this.greaterThanEqual((IntegerValue) other);
            case "==": return this.equal((IntegerValue) other);
            case "!=": return this.notEqual((IntegerValue) other);
        }
        throw new InvalidOperationAppException("InvalidOperationAppException: Cannot compose two different types using operator " + operation);
    }

    @Override
    public IType getType(){
        return new IntegerType();
    }

    @Override
    public boolean equals(IValue other) {
        if(other.getType() instanceof IntegerType)
            return this.getValue() == ((IntegerValue) other).getValue();
        return false;
    }

    public int getValue(){
        return this.value;
    }
}
