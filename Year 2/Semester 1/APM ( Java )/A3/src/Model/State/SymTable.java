package Model.State;

import Model.ADT.MyDictionary;
import Model.ADT.MyIDictionary;
import Model.Exception.ADTException;
import Model.Exception.AppException;
import Model.State.Exceptions.SymbolAlreadyExistsAppException;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.Values.IValue;
import Model.Values.Types.IType;

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


}
