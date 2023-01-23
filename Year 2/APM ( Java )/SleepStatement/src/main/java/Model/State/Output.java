package Model.State;

import Model.ADT.MyIList;
import Model.ADT.MyList;

import java.util.List;

public class Output implements IOutput{
    MyIList<String> data;

    public Output(){
        this.data = new MyList<>();
    }

    @Override
    public List<String> getOutputAsList(){
        return this.data.getAll();
    }

    @Override
    public String getOutput() {
        StringBuilder ans = new StringBuilder();
        for(String elem: this.data.getAll())
            ans.append(elem).append(" ");
        return ans.toString();
    }

    @Override
    public void appendToOutput(String string){
        this.data.add(string);
    }

    @Override
    public void setOutput(String string){
        this.data.clear();
        this.data.add(string);
    }

    @Override
    public String toString(){
        return "Output: " + this.getOutput() + " ";
    }



}
