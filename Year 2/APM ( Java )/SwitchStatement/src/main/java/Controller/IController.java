package Controller;

import Model.Exception.AppException;
import Model.State.ProgState;
import Model.Statements.IStatement;

import java.util.List;


public interface IController {

    public void executeOneStep() throws AppException;
    public void executeAllSteps() throws AppException;
    public void displayCurrentState() throws AppException;

    public void removeCompletedPrograms();
    public void setDisplayFlag(boolean displayFlag);

    public void setProgram(IStatement statement) throws AppException;
    public boolean getDisplayFlag();

    public List<ProgState> getProgStates();
}
