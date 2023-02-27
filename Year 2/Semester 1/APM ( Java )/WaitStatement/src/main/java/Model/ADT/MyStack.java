package Model.ADT;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;
import Model.Exception.ADTException;


public class MyStack<T> implements MyIStack<T>{
    private Stack<T> stack;

    public MyStack(){
        this.stack = new Stack<T>();
    }

    @Override
    public void push(T elem){
        this.stack.push(elem);
    }

    @Override
    public T pop() throws ADTException{
        if(this.stack.isEmpty())
            throw new ADTException("Empty stack");
        return this.stack.pop();
    }

    @Override
    public boolean isEmpty(){
        return this.stack.empty();
    }

    @Override
    public List<T> getReversed(){
        List<T> l = new ArrayList<T>(this.stack);
        Collections.reverse(l);
        return l;
    }

    @Override
    public int size(){
        return this.stack.size();
    }

    @Override
    public T top() throws ADTException{
        if(this.stack.isEmpty())
            throw new ADTException("Cannot pop from an empty stack!");
        return this.stack.peek();
    }

    @Override
    public List<T> toList() {
        return this.stack.stream().toList();
    }
}
