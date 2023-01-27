package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;

public class NewLockStatement implements IStatement{

    IExpression variable;

    public NewLockStatement(IExpression expression){
        this.variable = expression;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        try {
            IValue found_index = progState.getSymTable().getValue(this.variable.toString());
            int i = progState.getLockTable().newLock();
            progState.getSymTable().setValue(this.variable.toString(), new IntegerValue(i));
        }
        catch (SymbolNotFoundAppException e){
            throw new AppException(e.getMessage());
        }
        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if(!(new IntegerType()).equals(this.variable.typeCheck(typeEnv)))
            throw new AppException("Newlock doesn't have int argument!");
        return typeEnv;
    }

    @Override
    public String toString(){
        return "NewLock(" + this.variable.toString() + ")";
    }
}
