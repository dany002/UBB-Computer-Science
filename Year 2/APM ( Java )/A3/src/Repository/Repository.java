package Repository;

import Model.State.ProgState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Repository implements IRepository{
    List<ProgState> programs;
    String logFilePath;

    public Repository(String logFilePath)
    {
        this.programs = new ArrayList<>();
        this.logFilePath = logFilePath;
    }

    @Override
    public ProgState getCurrentProgram() {
        return this.programs.get(0);
    }

    @Override
    public void addProgram(ProgState program){
        this.programs.add(program);
    }

    @Override
    public void logProgramState(){
        if(this.logFilePath != null){
            PrintWriter logFile = null;
            try{
                logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
            } catch(IOException e){
                throw new RuntimeException(e);
            }
            logFile.println(this.programs.get(0).toString());
            logFile.close();
        }
    }
    @Override
    public void clear(){
        this.programs = new ArrayList<>();
    }
}
