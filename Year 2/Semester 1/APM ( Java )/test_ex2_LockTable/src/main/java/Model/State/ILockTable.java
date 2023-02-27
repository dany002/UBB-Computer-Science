package Model.State;

import Model.Exception.ADTException;

import java.util.Map;

public interface ILockTable {

    public int newLock();

    public boolean realLock(int address,int id) throws ADTException;

    public void unlock(int address, int id) throws ADTException;

    public Map<Integer,Integer> toMap();
}
