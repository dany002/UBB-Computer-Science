package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ExecutionStack;
import Model.State.ProgState;
import Model.Values.Types.IType;

public class ForkStatement implements IStatement{

    IStatement innerStatement;

    public ForkStatement(IStatement statement){
        this.innerStatement = statement;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        return new ProgState(new ExecutionStack(), progState.getSymTable().copy(), progState.getOutput(), progState.getFileTable(), progState.getHeap(), progState.getLatchTable(), this.innerStatement);
    }

    @Override
    public String toString(){
        return "fork(" + this.innerStatement.toString() + ")";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        return this.innerStatement.typeCheck(typeEnv.copy());
    }
}
