package Model.State;

import Model.ADT.MyDictionary;
import Model.ADT.MyIDictionary;
import Model.Exception.ADTException;
import Model.Exception.AppException;
import Model.State.Exceptions.SymbolAlreadyExistsAppException;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.Values.IValue;
import Model.Values.Types.IType;

import java.util.Map;

public class SymTable implements ISymTable{
    MyIDictionary<String, IValue> data;

    public SymTable(){
        this.data = new MyDictionary<>();
    }

    @Override
    public void declValue(String name, IType type) throws SymbolAlreadyExistsAppException{
        if(this.data.isVarDef(name))
            throw new SymbolAlreadyExistsAppException("Symbol " + name + " already exists.");
        this.data.put(name, type.getDefaultValue());
    }

    @Override
    public IValue getValue(String name) throws SymbolNotFoundAppException{
        try{
            return this.data.LookUp(name);
        }
        catch(ADTException exception){
            throw new SymbolNotFoundAppException("Symbol " + name + " not found.");
        }
    }

    @Override
    public void setValue(String name, IValue value) throws SymbolNotFoundAppException, ADTException {
        if(!this.data.isVarDef(name))
            throw new SymbolNotFoundAppException("Symbol " + name + " not found.");
        if(!this.data.LookUp(name).getType().equals(value.getType()))
            throw new SymbolNotFoundAppException("Symbol" + name + " does not have the same type as new value.");
        this.data.update(name, value);
    }

    @Override
    public String toString(){
        StringBuilder ans = new StringBuilder("SymTable: \n");
        try{
            for(String key : this.data.getKeys())
                ans.append(key).append("(").append(this.data.LookUp(key).getType().toString()).append(")").append(":-> ").append(this.data.LookUp(key).toString()).append('\n');
        }
        catch(AppException exception){
            throw new RuntimeException(exception.getMessage());
        }
        return ans.toString();
    }

    @Override
    public ISymTable copy() throws AppException{
        ISymTable newSymTable = new SymTable();

        for(String key: this.data.getKeys()){
            newSymTable.declValue(key, this.data.LookUp(key).getType());
            newSymTable.setValue(key, this.data.LookUp(key).clone());
        }

        return newSymTable;
    }

    @Override
    public Map<String, IValue> toMap(){
        return this.data.toMap();
    }

}
