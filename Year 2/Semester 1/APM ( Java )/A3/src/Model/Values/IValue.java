package Model.Values;

import Model.Values.Exceptions.DivisionOverflowAppException;
import Model.Values.Exceptions.InvalidOperationAppException;
import Model.Values.Types.IType;

public interface IValue {
    public String toString();
    public IValue compose(IValue other, String operation) throws InvalidOperationAppException, DivisionOverflowAppException;
    public IType getType();

    public boolean equals(IValue other);
}
