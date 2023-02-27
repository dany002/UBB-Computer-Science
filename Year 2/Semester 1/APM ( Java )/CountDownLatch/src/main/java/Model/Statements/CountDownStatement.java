package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.Exceptions.AddressOutOfBoundsAppException;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.Types.IType;

public class CountDownStatement implements IStatement{

    String name;

    public CountDownStatement(String name){
        this.name = name;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        try{
            IValue foundIndex = progState.getSymTable().getValue(this.name);
            progState.getLatchTable().countDown(((IntegerValue)foundIndex).getValue());
            progState.getOutput().appendToOutput(Integer.toString(progState.getId()));
            }
        catch (SymbolNotFoundAppException e){
            throw new AppException("AwaitStatementError: " + this.name + " is not in the sym table.");
        }
        catch(AddressOutOfBoundsAppException ex){
            return null;
        }
        return null;
    }

    @Override
    public String toString(){
        return "countDown(" + this.name + ")";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        return typeEnv;
    }
}
