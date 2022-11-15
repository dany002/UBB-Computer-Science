package Model.Values.Types;

import Model.Values.IValue;

public interface IType {
    public IValue getDefaultValue();
    public String toString();
}
