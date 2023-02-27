package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.ADTException;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.Expressions.VariableExpression;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;

public class LockStatement implements IStatement{

    IExpression name;

    public LockStatement(IExpression etc){
        this.name = etc;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        boolean x = false;
        try {
            IValue found_index = progState.getSymTable().getValue(this.name.toString());
            try{
                x = progState.getLockTable().realLock(((IntegerValue)found_index).getValue(), progState.getId());
            }catch (ADTException f){
                throw new AppException(f.getMessage());
            }
        }
        catch (SymbolNotFoundAppException e){
            throw new AppException(e.getMessage());
        }
        if(!x){
            progState.getExecutionStack().push(new LockStatement(this.name));
        }
        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if(!(new IntegerType()).equals(this.name.typeCheck(typeEnv)))
            throw new AppException("Lock doesn't have int argument!");
        return typeEnv;
    }

    @Override
    public String toString(){
        return "Lock(" + this.name.toString() + ")";
    }
}
