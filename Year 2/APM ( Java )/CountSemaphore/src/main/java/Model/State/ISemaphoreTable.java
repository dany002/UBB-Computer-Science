package Model.State;

import Model.Exception.ADTException;
import Model.State.Exceptions.AddressOutOfBoundsAppException;
import javafx.util.Pair;

import java.util.ArrayList;
import java.util.Map;

public interface ISemaphoreTable {

    public int createSemaphore(int value);

    public Pair<Integer, ArrayList<Integer>> acquire_release(int address) throws AddressOutOfBoundsAppException;

    public void addElementInAList(int address,int value) throws ADTException;

    public void removeElementFromAList(int address, int value) throws ADTException;

    public Map<Integer,Pair<Integer,ArrayList<Integer>>> toMap();



}
