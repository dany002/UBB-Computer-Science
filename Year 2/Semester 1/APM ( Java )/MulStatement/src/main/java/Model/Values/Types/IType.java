package Model.Values.Types;

import Model.Exception.AppException;
import Model.Values.IValue;

public interface IType {
    public IValue getDefaultValue();
    public String toString();

    public boolean equals(IType other);

    public IType compose(String operation) throws AppException;
}
