package Model.State;

import Model.ADT.MyIStack;
import Model.ADT.MyStack;
import Model.Exception.ADTException;
import Model.Statements.IStatement;

public class ExecutionStack implements IExecutionStack{
    MyIStack<IStatement> stack;

    public ExecutionStack(){
        this.stack = new MyStack<>();
    }

    @Override
    public IStatement pop() throws ADTException{
        return this.stack.pop();
    }

    @Override
    public void push(IStatement statement){
        this.stack.push(statement);
    }

    @Override
    public boolean empty(){
        return this.stack.isEmpty();
    }

    @Override
    public int size(){
        return this.stack.size();
    }

    @Override
    public String toDebug(){
        StringBuilder ans = new StringBuilder("Execution stack:\n");
        MyIStack<IStatement> tmp = new MyStack<>();
        try{
            while(!this.stack.isEmpty()){
                tmp.push(this.stack.pop());
                ans.append(tmp.top().toString()).append('\n');
            }
            while(!tmp.isEmpty())
                this.stack.push(tmp.pop());
        }
        catch(ADTException exception){
            throw new RuntimeException(exception.getMessage());
        }
        return ans.toString();
    }
}
