package Controller;

import Model.Exception.ADTException;
import Model.Exception.AppException;
import Model.State.*;
import Model.Statements.IStatement;
import Model.Statements.IfStatement;
import Model.Statements.NoOperationStatement;
import Repository.IRepository;
import Repository.Repository;

import java.util.concurrent.ExecutorService;
import java.util.stream.Collectors;

public class Controller implements IController{
    IRepository repo;
    boolean displayFlag;
    ExecutorService executor;


    public Controller(boolean displayFlag){

        this.displayFlag = displayFlag;
        if(this.displayFlag)
            this.displayCurrentState();
    }

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
        ProgState state = this.repo.getCurrentProgram();
        IStatement statement = state.getExecutionStack().pop();
        statement.execute(state);
        if(this.displayFlag)
            this.displayCurrentState();
        this.repo.logProgramState();
    }

    @Override
    public void setProgram(IStatement statement){
        this.repo.clear();
        this.repo.addProgram(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), statement));
        this.repo.logProgramState();
        if(this.displayFlag)
            this.displayCurrentState();
    }

    @Override
    public void executeAllSteps() throws AppException{
        try{
            while(true)
                this.executeOneStep();
        }
        catch(ADTException exception){
            ;
        }
        catch(AppException e){
            this.setProgram(new NoOperationStatement());
            throw e;
        }
    }

    @Override
    public void displayCurrentState() {
        System.out.println(this.repo.getCurrentProgram().toString() + "\n");
    }


}



































