package Model.State;

import Model.ADT.MyDictionary;
import Model.ADT.MyIDictionary;
import Model.Exception.ADTException;
import Model.State.Exceptions.AddressOutOfBoundsAppException;
import javafx.util.Pair;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.locks.ReentrantLock;

public class SemaphoreTable implements ISemaphoreTable{

    MyIDictionary<Integer,Pair<Integer, ArrayList<Integer>>> data;

    int firstFree;

    ReentrantLock lock;

    public SemaphoreTable(){
        this.data = new MyDictionary<>();
        this.firstFree = 1;
        this.lock = new ReentrantLock();
    }

    @Override
    public int createSemaphore(int value) {
        this.lock.lock();
        ArrayList<Integer> empty_list = new ArrayList<>();
        Pair<Integer,ArrayList<Integer>> first_elem = new Pair<>(value,empty_list);
        this.data.put(this.firstFree, first_elem);
        this.firstFree++;
        this.lock.unlock();
        return this.firstFree - 1;

    }

    @Override
    public Pair<Integer, ArrayList<Integer>> acquire_release(int address) throws AddressOutOfBoundsAppException {
        try{
            this.lock.lock();
            return this.data.LookUp(address);

        } catch (ADTException e) {
            throw new AddressOutOfBoundsAppException("Address " + Integer.toString(address) + " is out of bounds.");
        } finally {
            this.lock.unlock();
        }
    }

    @Override
    public void addElementInAList(int address,int value) throws ADTException {

        this.lock.lock();
        ArrayList<Integer> old_list = this.data.LookUp(address).getValue();
        old_list.add(value);
        Pair<Integer,ArrayList<Integer>> etc = new Pair<>(this.data.LookUp(address).getKey(), old_list);
        this.data.update(address, etc);
        this.lock.unlock();
    }

    @Override
    public void removeElementFromAList(int address, int value) throws ADTException {
        this.lock.lock();
        ArrayList<Integer> old_list = this.data.LookUp(address).getValue();
        old_list.remove(Integer.valueOf(value));
        Pair<Integer,ArrayList<Integer>> etc = new Pair<>(this.data.LookUp(address).getKey(), old_list);
        this.data.update(address, etc);
        this.lock.unlock();
    }

    @Override
    public Map<Integer, Pair<Integer, ArrayList<Integer>>> toMap() {
        return this.data.toMap();
    }

    @Override
    public String toString(){
        StringBuilder ans = new StringBuilder("SemaphoreTable:\n");
        try{
            for(int key: this.data.getKeys())
                ans.append(key).append(":-> ").append(this.data.LookUp(key).toString()).append("\n");
        } catch(ADTException e){
            throw new RuntimeException(e.getMessage());
        }
        return ans.toString();
    }
}
