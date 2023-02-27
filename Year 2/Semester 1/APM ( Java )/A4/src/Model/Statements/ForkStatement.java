package Model.Statements;

import Model.Exception.AppException;
import Model.State.ExecutionStack;
import Model.State.ProgState;

public class ForkStatement implements IStatement{

    IStatement innerStatement;

    public ForkStatement(IStatement statement){
        this.innerStatement = statement;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        return new ProgState(new ExecutionStack(), progState.getSymTable().copy(), progState.getOutput(), progState.getFileTable(), progState.getHeap(), this.innerStatement);
    }

    @Override
    public String toString(){
        return "fork(" + this.innerStatement.toString() + ")";
    }
}
