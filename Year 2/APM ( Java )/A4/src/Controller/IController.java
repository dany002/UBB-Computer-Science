package Controller;

import Model.Exception.AppException;
import Model.Statements.IStatement;


public interface IController {

    public void executeOneStep() throws AppException;
    public void executeAllSteps() throws AppException;
    public void displayCurrentState();

    public void removeCompletedPrograms();
    public void setDisplayFlag(boolean displayFlag);

    public void setProgram(IStatement statement);
    public boolean getDisplayFlag();
}
