package Model.ADT;
import Model.Exception.ADTException;

import java.util.List;
import java.util.Map;

public interface MyIDictionary<K,V> {
    public void put(K key, V value);

    public V LookUp(K key) throws ADTException;

    public boolean isVarDef(K key);

    public void update(K key, V value) throws ADTException;

    public String toString();

    public List<K> getKeys();

    public void removeKey(K Key) throws ADTException;

    public Map<K, V> toMap();

    public MyIDictionary<K, V> copy();
}
