package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.ADTException;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;

public class UnlockStatement implements IStatement{

    IExpression name;

    public UnlockStatement(IExpression ect){
        this.name = ect;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        try {
            IValue found_index = progState.getSymTable().getValue(this.name.toString());
            try{
                progState.getLockTable().unlock(((IntegerValue)found_index).getValue(), progState.getId());
            }catch (ADTException f){
                throw new AppException(f.getMessage());
            }
        }
        catch (SymbolNotFoundAppException e){
            throw new AppException(e.getMessage());
        }
        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if(!(new IntegerType()).equals(this.name.typeCheck(typeEnv)))
            throw new AppException("Unlock doesn't have int argument!");
        return typeEnv;
    }

    @Override
    public String toString(){
        return "Unlock( " + this.name.toString() + ")";
    }
}
