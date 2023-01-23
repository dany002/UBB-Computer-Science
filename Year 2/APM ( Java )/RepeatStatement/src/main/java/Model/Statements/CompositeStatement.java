package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Values.Types.IType;

public class CompositeStatement implements IStatement{
    IStatement firstStatement;
    IStatement secondStatement;

    public CompositeStatement(IStatement firstStatement, IStatement secondStatement) {
        this.firstStatement = firstStatement;
        this.secondStatement = secondStatement;
    }

    @Override
    public ProgState execute(ProgState state){
        state.getExecutionStack().push(this.secondStatement);
        state.getExecutionStack().push(this.firstStatement);
        return null;
    }

    @Override
    public String toString(){
        return this.firstStatement + "; " + this.secondStatement;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        return this.secondStatement.typeCheck(this.firstStatement.typeCheck(typeEnv));
    }
}
