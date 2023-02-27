package Model.State;

import Model.ADT.MyDictionary;
import Model.ADT.MyIDictionary;
import Model.Exception.ADTException;
import Model.State.Exceptions.AddressOutOfBoundsAppException;
import Model.Values.IValue;

import java.util.Map;
import java.util.concurrent.locks.ReentrantLock;

public class LatchTable implements ILatchTable{

    MyIDictionary<Integer,Integer> data;
    int firstFree;

    ReentrantLock lock;

    public LatchTable(){
        this.data = new MyDictionary<>();
        this.firstFree = 1;
        this.lock = new ReentrantLock();
    }

    @Override
    public int newLatch(int value) {
        this.lock.lock();
        this.data.put(this.firstFree, value);
        this.firstFree++;
        this.lock.unlock();
        return this.firstFree - 1;
    }

    @Override
    public int await(int address) throws AddressOutOfBoundsAppException {
        try{
            this.lock.lock();
            int a = this.data.LookUp(address);
            return a;
        } catch (ADTException e) {
            throw new AddressOutOfBoundsAppException("Address " + Integer.toString(address) + " is out of bounds.");
        } finally{
            this.lock.unlock();
        }
    }

    @Override
    public void countDown(int address) throws AddressOutOfBoundsAppException {
        try{
            this.lock.lock();
            int found = this.data.LookUp(address);
            if(found > 0)
                this.data.update(address, found-1);
        }
        catch(ADTException e){
            throw new AddressOutOfBoundsAppException("Address " + Integer.toString(address) + " is out of bounds.");
        }finally {
            this.lock.unlock();
        }
    }


    @Override
    public Map<Integer, Integer> toMap() {
        return this.data.toMap();
    }

    @Override
    public String toString(){
        StringBuilder ans = new StringBuilder("LatchTable:\n");
        try{
            for(int key: this.data.getKeys())
                ans.append(key).append(":-> ").append(this.data.LookUp(key).toString()).append("\n");
        } catch(ADTException e){
            throw new RuntimeException(e.getMessage());
        }
        return ans.toString();
    }
}
