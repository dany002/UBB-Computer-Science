package Model.Statements;

import Model.Exception.AppException;
import Model.State.ProgState;

public interface IStatement {
    public ProgState execute(ProgState progState) throws AppException;
    public String toString();
}
