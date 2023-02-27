package Model.State;

import Model.ADT.MyDictionary;
import Model.ADT.MyIDictionary;
import Model.Exception.ADTException;
import Model.Values.IValue;

import java.util.Map;
import java.util.concurrent.locks.ReentrantLock;

public class LockTable implements ILockTable{

    int freeLocation;
    MyIDictionary<Integer,Integer> data;
    ReentrantLock lock;

    public LockTable(){
        this.data = new MyDictionary<>();
        this.freeLocation = 1;
        this.lock = new ReentrantLock();
    }

    @Override
    public int newLock() {
        this.lock.lock();
        this.data.put(this.freeLocation, -1);
        this.freeLocation++;
        this.lock.unlock();
        return this.freeLocation - 1;
    }

    @Override
    public boolean realLock(int address,int id) throws ADTException {
        this.lock.lock();
        try{
            int a = this.data.LookUp(address);
            if(a == -1)
                this.data.update(address, id);
            return true;
        }catch (ADTException e){
            throw new ADTException(e.getMessage());
        } finally {
            this.lock.unlock();
        }
    }

    @Override
    public void unlock(int address, int id) throws ADTException{
        this.lock.lock();
        try{
            int a = this.data.LookUp(address);
            if(a == id)
                this.data.update(address, -1);
        }catch (ADTException e){
            throw new ADTException(e.getMessage());
        } finally {
            this.lock.unlock();
        }
    }

    @Override
    public Map<Integer, Integer> toMap() {
        return this.data.toMap();
    }

    @Override
    public String toString(){
        StringBuilder ans = new StringBuilder("LockTable:\n");
        try{
            for(int key: this.data.getKeys())
                ans.append(key).append(":-> ").append(this.data.LookUp(key).toString()).append("\n");
        } catch(ADTException e){
            throw new RuntimeException(e.getMessage());
        }
        return ans.toString();
    }

}
