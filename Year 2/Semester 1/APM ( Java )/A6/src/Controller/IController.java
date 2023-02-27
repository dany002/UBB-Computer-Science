package Controller;

import Model.Exception.AppException;
import Model.Statements.IStatement;


public interface IController {

    public void executeOneStep() throws AppException;
    public void executeAllSteps() throws AppException;
    public void displayCurrentState() throws AppException;

    public void removeCompletedPrograms();
    public void setDisplayFlag(boolean displayFlag);

    public void setProgram(IStatement statement) throws AppException;
    public boolean getDisplayFlag();
}
