package Controller;

import Model.State.Exceptions.AddressOutOfBoundsAppException;
import Model.State.IHeap;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.RefValue;
import Model.Values.Types.RefType;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class GarbageCollector {
    public static void runGarbageCollector(List<ProgState> states){
        if(states.size() < 1)
            return;
        IHeap heap = states.get(0).getHeap();
        List<Integer> activeAddresses = states.stream().flatMap(e -> GarbageCollector.getActiveAddressesForState(e).stream()).toList();
        heap.toMap().keySet().stream().filter(e -> !activeAddresses.contains(e)).forEach(e -> {
            try{
                heap.deallocate(e);
            } catch(AddressOutOfBoundsAppException ex){
                throw new RuntimeException(ex);
            }
        });
    }
    public static List<Integer> getActiveAddressesForState(ProgState state){
        return state.getSymTable().toMap().values().stream()
                .filter(e -> e.getType() instanceof RefType)
                .map(e -> (RefValue) e)
                .flatMap(value -> {
                    List<Integer> addresses = new ArrayList<Integer>();
                    while(true){
                        if(value.getAddress() == 0)
                            break;
                        addresses.add(value.getAddress());
                        IValue next_value;
                        try{
                            next_value = state.getHeap().read(value.getAddress());
                        } catch (AddressOutOfBoundsAppException e){
                            throw new RuntimeException(e);
                        }
                        if(!(next_value.getType() instanceof RefType))
                            break;
                        value = (RefValue) next_value;
                    }
                    return addresses.stream();
                }).collect(Collectors.toList());
    }
}

