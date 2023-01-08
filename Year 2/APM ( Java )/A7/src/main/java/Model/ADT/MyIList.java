package Model.ADT;

import java.util.List;

public interface MyIList<T> {
    public void add(T elem);

    public String toString();

    public List<T> getAll();

    public void clear();

}
