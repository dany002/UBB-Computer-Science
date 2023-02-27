package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.Expressions.VariableExpression;
import Model.State.Exceptions.AddressOutOfBoundsAppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.StringValue;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;
import javafx.util.Pair;

import java.util.ArrayList;

public class AcquireStatement implements IStatement{

    IExpression variable;

    public AcquireStatement(IExpression variable){
        this.variable = variable;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue foundIndex = progState.getSymTable().getValue(this.variable.toString());
        try{
            Pair<Integer, ArrayList<Integer>> keyInSemaphoreTable = progState.getSemaphoreTable().acquire_release(((IntegerValue)foundIndex).getValue());
            int nl = keyInSemaphoreTable.getValue().size();
            if(nl < keyInSemaphoreTable.getKey()){
                int a = keyInSemaphoreTable.getValue().indexOf(progState.getId());
                if(a == -1)
                    progState.getSemaphoreTable().addElementInAList(keyInSemaphoreTable.getKey(),progState.getId());
            }
            else
                progState.getExecutionStack().push(new AcquireStatement(new VariableExpression(this.variable.toString())));
        }catch (AddressOutOfBoundsAppException e){
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
        return "Acquire(" + this.variable.toString() + ")";
    }
}
