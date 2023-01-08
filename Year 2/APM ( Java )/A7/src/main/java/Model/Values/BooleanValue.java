package Model.Values;

import Model.Values.Exceptions.InvalidOperationAppException;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IType;

public class BooleanValue implements IValue{
    boolean value;

    public BooleanValue(){
        this.value = false;
    }

    public BooleanValue(boolean new_value){
        this.value = new_value;
    }

    public BooleanValue and(BooleanValue other){
        return new BooleanValue(this.value & other.value);
    }

    public BooleanValue or(BooleanValue other){
        return new BooleanValue(this.value | other.value);
    }

    private BooleanValue equal(BooleanValue other){
        return new BooleanValue(this.equals(other));
    }

    private BooleanValue notEqual(BooleanValue other){
        return new BooleanValue(!this.equals(other));
    }

    @Override
    public String toString(){
        return Boolean.toString(this.value);
    }

    @Override
    public IValue compose(IValue other, String operation) throws InvalidOperationAppException {
        if(!(other.getType() instanceof BooleanType))
            throw new InvalidOperationAppException("InvalidOperationAppException: Cannot compose two different types using operation " + operation);
        switch (operation){
            case "and" : return this.and((BooleanValue) other);
            case "or" : return this.or((BooleanValue) other);
            case "==" : return this.equal((BooleanValue) other);
            case "!=" : return this.notEqual((BooleanValue) other);
        }
        throw new InvalidOperationAppException("InvalidOperationAppException: Cannot compose two different types using operation " + operation);
    }

    @Override
    public IType getType(){
        return new BooleanType();
    }

    public boolean getValue(){
        return this.value;
    }

    @Override
    public boolean equals(IValue other){
        if(other.getType() instanceof BooleanType)
            return this.getValue() == ((BooleanValue) other).getValue();
        return false;
    }

    @Override
    public IValue clone(){
        return new BooleanValue(this.value);
    }
}
