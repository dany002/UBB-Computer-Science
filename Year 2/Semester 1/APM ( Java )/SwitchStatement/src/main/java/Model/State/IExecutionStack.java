package Model.State;

import Model.Exception.ADTException;
import Model.Statements.IStatement;

import java.util.List;

public interface IExecutionStack {
    public IStatement pop() throws ADTException;
    public void push(IStatement statement);
    public boolean empty();
    public int size();
    public String toString();

    public List<IStatement> toList();
}
