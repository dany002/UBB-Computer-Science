package Model.ADT;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements MyIList<T>{
    private List<T> out;

    public MyList(){
        this.out = new ArrayList<T>();
    }

    @Override
    public void add(T elem){
        this.out.add(elem);
    }

    @Override
    public String toString(){
        return this.out.toString();
    }

    @Override
    public void clear(){
        this.out.clear();
    }

    @Override
    public List<T> getAll(){
        return this.out;
    }

}
