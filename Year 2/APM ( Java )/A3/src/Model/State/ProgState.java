package Model.State;

import Model.ADT.MyDictionary;
import Model.ADT.MyIStack;
import Model.ADT.MyStack;
import Model.Statements.IStatement;

public class ProgState {
    IExecutionStack executionStack;
    ISymTable symTable;
    IOutput output;

    IFileTable fileTable;

    public ProgState(IExecutionStack executionStack, ISymTable symTable, IOutput output, IFileTable fileTable, IStatement statement) {
        this.executionStack = executionStack;
        this.symTable = symTable;
        this.output = output;
        this.fileTable = fileTable;
        this.executionStack.push(statement);
    }


    public IExecutionStack getExecutionStack(){
        return this.executionStack;
    }

    public ISymTable getSymTable(){
        return this.symTable;
    }

    public IOutput getOutput(){
        return this.output;
    }

    public IFileTable getFileTable(){
        return this.fileTable;
    }

    @Override
    public String toString(){
        return this.executionStack.toString().strip() + "\n" + this.symTable.toString().strip() + "\n" + this.output.toString().strip() + "\n" + this.fileTable.toString().strip();
    }
}
