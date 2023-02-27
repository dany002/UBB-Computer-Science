package Model.Statements;

import Model.Exception.AppException;
import Model.State.ProgState;

public interface IStatement {
    public void execute(ProgState progState) throws AppException;
    public String toString();
}
