package Model.State;

import Model.State.Exceptions.AddressOutOfBoundsAppException;
import Model.Values.IValue;

import java.util.Map;

public interface IHeap {
    public int allocate(IValue value);

    public IValue read(int address) throws AddressOutOfBoundsAppException;

    public void write(int address, IValue value) throws AddressOutOfBoundsAppException;

    public void deallocate(int address) throws AddressOutOfBoundsAppException;

    public Map<Integer, IValue> toMap();
}
