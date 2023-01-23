package Controller;

import Model.ADT.MyDictionary;
import Model.Exception.ADTException;
import Model.Exception.AppException;
import Model.State.*;
import Model.Statements.IStatement;
import Model.Statements.IfStatement;
import Model.Statements.NoOperationStatement;
import Repository.IRepository;
import Repository.Repository;

import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.stream.Collectors;

public class Controller implements IController{
    IRepository repo;
    boolean displayFlag;
    ExecutorService executor;


    public Controller(IRepository repo, ExecutorService executor, boolean displayFlag){
        this.executor = executor;
        this.displayFlag = displayFlag;
        this.repo = repo;
    }

    @Override
    public void removeCompletedPrograms(){
        this.repo.setProgramsList(this.repo.getProgramsList().stream().filter(ProgState::isNotCompleted).collect(Collectors.toList()));
    }

    @Override
    public boolean getDisplayFlag(){
        return this.displayFlag;
    }

    @Override
    public void setDisplayFlag(boolean displayFlag){
        this.displayFlag = displayFlag;
    }

    @Override
    public void executeOneStep() throws AppException{
        this.removeCompletedPrograms();
        List<Callable<ProgState>> stepList = this.repo.getProgramsList().stream().map(program -> (Callable<ProgState>) (() -> {
            return program.executeOneStep();
        })).toList();
        List<ProgState> newPrograms = null;
        try{
            newPrograms = executor.invokeAll(stepList).stream().map(future -> {
                try{
                    return future.get();
                } catch(InterruptedException e){
                    throw new RuntimeException(e);
                } catch(ExecutionException e) {
                    System.out.println(e);
                    try {
                        this.setProgram(new NoOperationStatement());
                    } catch (AppException ex) {
                        throw new RuntimeException(ex);
                    }
                    throw new RuntimeException(e);
                }

            })
                    .filter(p -> p != null).toList();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        newPrograms.forEach(e -> this.repo.addProgram(e));
        GarbageCollector.runGarbageCollector(this.repo.getProgramsList());

        if(this.displayFlag)
            this.displayCurrentState();
        this.repo.getProgramsList().forEach(e -> this.repo.logProgramState(e));
    }

    @Override
    public void setProgram(IStatement statement) throws AppException{
        statement.typeCheck(new MyDictionary<>());
        this.repo.clear();
        this.repo.addProgram(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), new Heap(), statement));
        this.repo.logProgramState(this.repo.getProgramsList().get(0));
        if(this.displayFlag)
            this.displayCurrentState();
    }

    @Override
    public void executeAllSteps() throws AppException{
        while(true){
            this.removeCompletedPrograms();
            if(this.repo.getProgramsList().size() == 0)
                break;
            this.executeOneStep();
        }
    }

    @Override
    public void displayCurrentState() throws AppException{
        this.repo.getProgramsList().forEach(program -> System.out.println(program.toString() + '\n'));
    }

    @Override
    public List<ProgState> getProgStates(){
        return this.repo.getProgramsList();
    }

}



































