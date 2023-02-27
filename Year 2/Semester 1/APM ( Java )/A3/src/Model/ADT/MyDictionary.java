package Model.ADT;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import Model.Exception.ADTException;

public class MyDictionary<K,V> implements MyIDictionary<K,V>{
    private Map<K,V> map;

    public MyDictionary() {
        this.map = new HashMap<>();
    }

    @Override
    public void put(K key, V value){
        this.map.put(key,value);
    }

    @Override
    public V LookUp(K key) throws ADTException {
        V value = this.map.get(key);
        if(value == null)
            throw new ADTException("ID not defined");
        return value;
    }

    @Override
    public boolean isVarDef(K key){
        return this.map.containsKey(key);
    }

    @Override
    public void update(K key, V value) throws ADTException{
        if(!this.isVarDef(key))
            throw new ADTException("ID not found");
        this.map.put(key, value);
    }

    @Override
    public String toString(){
        return this.map.toString();
    }

    @Override
    public List<K> getKeys(){
        return new ArrayList<>(this.map.keySet());
    }

    @Override
    public void removeKey(K key) throws ADTException{
        this.map.remove(key);
    }
}
