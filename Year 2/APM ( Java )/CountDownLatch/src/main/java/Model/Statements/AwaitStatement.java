package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.Exceptions.AddressOutOfBoundsAppException;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.Types.IType;

public class AwaitStatement implements IStatement{

    String name;

    public AwaitStatement(String name){
        this.name = name;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        int value;
        try{
            IValue foundIndex = progState.getSymTable().getValue(this.name);
            try{
                value = progState.getLatchTable().await(((IntegerValue)foundIndex).getValue());
            }
            catch (AddressOutOfBoundsAppException w){
                throw new AppException("AwaitStatementError: " + this.name + " is not in the LatchTable.");
            }
        } catch (SymbolNotFoundAppException e){
            throw new AppException("AwaitStatementError: " + this.name + " is not in the sym table.");
        }
        if(value != 0){
            progState.getExecutionStack().push(new AwaitStatement(this.name));
        }
        return null;
    }

    @Override
    public String toString(){
        return "await(" + this.name + ")";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        return typeEnv;
    }
}
