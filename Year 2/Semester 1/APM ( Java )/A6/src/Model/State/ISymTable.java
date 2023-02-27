package Model.State;

import Model.Exception.ADTException;
import Model.Exception.AppException;
import Model.State.Exceptions.SymbolAlreadyExistsAppException;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.Values.IValue;
import Model.Values.Types.IType;

import java.util.Map;

public interface ISymTable {
    public void declValue(String name, IType type) throws SymbolAlreadyExistsAppException;
    public IValue getValue(String name) throws SymbolNotFoundAppException;
    public void setValue(String name, IValue value) throws SymbolNotFoundAppException, ADTException;
    public String toString();

    public ISymTable copy() throws AppException;

    public Map<String, IValue> toMap();
}
