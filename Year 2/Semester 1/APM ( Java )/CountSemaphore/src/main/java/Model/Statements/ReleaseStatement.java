package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.Exceptions.AddressOutOfBoundsAppException;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.StringValue;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;
import javafx.util.Pair;

import java.util.ArrayList;

public class ReleaseStatement implements IStatement{

    IExpression variable;

    public ReleaseStatement(IExpression variable){
        this.variable = variable;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        try {

            IValue found_index = progState.getSymTable().getValue(this.variable.toString());
            if(!(found_index.getType() instanceof IntegerType))
                throw new AppException("ReleaseStatement: The variable doesn't evaluate to int.");
            try{
                Pair<Integer, ArrayList<Integer>> listPair = progState.getSemaphoreTable().acquire_release(((IntegerValue)found_index).getValue());
                int index = listPair.getValue().indexOf(progState.getId());

                if(index != -1)
                    progState.getSemaphoreTable().removeElementFromAList(listPair.getKey(), progState.getId());
            } catch(AddressOutOfBoundsAppException f){
                throw new AppException(f.getMessage());
            }

        } catch (SymbolNotFoundAppException e ){
            throw new AppException(e.getMessage());
        }
        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if(!(new IntegerType()).equals(this.variable.typeCheck(typeEnv)))
            throw new AppException("AcquireStatement: The variable is not int.");
        return typeEnv;
    }

    @Override
    public String toString(){
        return "Release(" + this.variable.toString() + ")";
    }
}
