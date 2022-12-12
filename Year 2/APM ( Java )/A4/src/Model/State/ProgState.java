package Model.State;

import Model.ADT.MyDictionary;
import Model.ADT.MyIStack;
import Model.ADT.MyStack;
import Model.Exception.AppException;
import Model.Statements.IStatement;

public class ProgState {

    int id;
    static int nextId = 0;
    IExecutionStack executionStack;
    ISymTable symTable;
    IOutput output;
    IFileTable fileTable;
    IHeap heap;

    public ProgState(IExecutionStack executionStack, ISymTable symTable, IOutput output, IFileTable fileTable, IHeap heap, IStatement statement) {
        this.id = nextId;
        nextId++;
        this.executionStack = executionStack;
        this.symTable = symTable;
        this.output = output;
        this.fileTable = fileTable;
        this.heap = heap;
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

    public IHeap getHeap(){
        return this.heap;
    }

    public boolean isNotCompleted(){
        return this.executionStack.size() > 0;
    }

    public ProgState executeOneStep() throws AppException {
        IStatement statement = this.executionStack.pop();
        return statement.execute(this);
    }

    @Override
    public String toString(){
        return this.executionStack.toString().strip() + "\n" + this.symTable.toString().strip() + "\n" + this.output.toString().strip() + "\n" + this.fileTable.toString().strip() + "\n" + this.heap.toString().strip();
    }
}
