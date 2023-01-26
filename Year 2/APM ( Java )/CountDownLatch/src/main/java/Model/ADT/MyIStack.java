package Model.ADT;

import java.util.List;
import Model.Exception.ADTException;

public interface MyIStack<T> {

    public void push(T elem);

    public T pop() throws ADTException;

    public boolean isEmpty();

    public List<T> getReversed();

    public String toString();

    public int size();

    public T top() throws ADTException;

    public List<T> toList();
}
