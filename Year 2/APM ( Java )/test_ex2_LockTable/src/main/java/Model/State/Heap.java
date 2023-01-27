package Model.State;

import Model.ADT.MyDictionary;
import Model.ADT.MyIDictionary;
import Model.Exception.ADTException;
import Model.State.Exceptions.AddressOutOfBoundsAppException;
import Model.Values.IValue;

import java.util.Map;

public class Heap implements IHeap{

    MyIDictionary<Integer, IValue> heap;
    int firstFree;

    public Heap(){
        this.heap = new MyDictionary<>();
        this.firstFree = 1;
    }

    @Override
    public int allocate(IValue value) {
        this.heap.put(firstFree, value);
        this.firstFree++;
        return this.firstFree - 1;
    }

    @Override
    public IValue read(int address) throws AddressOutOfBoundsAppException {
        try{
            return this.heap.LookUp(address);
        }
        catch(ADTException e){
            throw new AddressOutOfBoundsAppException("Address" + Integer.toString(address) + " out of bounds.");
        }
    }

    @Override
    public void write(int address, IValue value) throws AddressOutOfBoundsAppException {
        if(!this.heap.getKeys().contains(address)){
            throw new AddressOutOfBoundsAppException("Address" + Integer.toString(address) + " out of bounds.");
        }
        this.heap.put(address, value);
    }

    @Override
    public void deallocate(int address) throws AddressOutOfBoundsAppException {
        try{
            this.heap.removeKey(address);
        } catch(ADTException e){
            throw new AddressOutOfBoundsAppException("Address" + Integer.toString(address) + " out of bounds.");
        }
    }

    @Override
    public Map<Integer, IValue> toMap() {
        return this.heap.toMap();
    }

    @Override
    public String toString(){
        StringBuilder ans = new StringBuilder("Heap:\n");
        try{
            for(int key: this.heap.getKeys())
                ans.append(key).append("(").append(this.heap.LookUp(key).getType().toString()).append(")").append(":-> ").append(this.heap.LookUp(key).toString()).append("\n");
        } catch(ADTException e){
            throw new RuntimeException(e.getMessage());
        }
        return ans.toString();
    }
}
