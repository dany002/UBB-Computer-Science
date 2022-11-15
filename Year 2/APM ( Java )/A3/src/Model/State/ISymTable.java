package Model.State;

import Model.Exception.ADTException;
import Model.State.Exceptions.SymbolAlreadyExistsAppException;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.Values.IValue;
import Model.Values.Types.IType;

public interface ISymTable {
    public void declValue(String name, IType type) throws SymbolAlreadyExistsAppException;
    public IValue getValue(String name) throws SymbolNotFoundAppException;
    public void setValue(String name, IValue value) throws SymbolNotFoundAppException, ADTException;
    public String toDebug();
}
