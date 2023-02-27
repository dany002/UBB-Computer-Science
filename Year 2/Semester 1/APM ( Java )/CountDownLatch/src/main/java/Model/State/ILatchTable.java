package Model.State;

import Model.State.Exceptions.AddressOutOfBoundsAppException;
import Model.Values.IValue;

import java.util.Map;

public interface ILatchTable {

    public int newLatch(int value);

    public int await(int address) throws AddressOutOfBoundsAppException;

    public void countDown(int address) throws AddressOutOfBoundsAppException;


    public Map<Integer, Integer> toMap();
}
