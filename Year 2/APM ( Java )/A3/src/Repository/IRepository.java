package Repository;

import Model.State.ProgState;

public interface IRepository {
    public ProgState getCurrentProgram();
    public void addProgram(ProgState program);

    public void logProgramState();

    public void clear();
}
