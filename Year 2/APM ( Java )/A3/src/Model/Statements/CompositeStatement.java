package Model.Statements;

import Model.State.ProgState;

public class CompositeStatement implements IStatement{
    IStatement firstStatement;
    IStatement secondStatement;

    public CompositeStatement(IStatement firstStatement, IStatement secondStatement) {
        this.firstStatement = firstStatement;
        this.secondStatement = secondStatement;
    }

    @Override
    public void execute(ProgState state){
        state.getExecutionStack().push(this.secondStatement);
        state.getExecutionStack().push(this.firstStatement);
    }

    @Override
    public String toString(){
        return this.firstStatement + "; " + this.secondStatement;
    }
}
