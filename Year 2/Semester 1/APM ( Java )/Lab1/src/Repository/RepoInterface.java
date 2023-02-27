package Repository;

import Model.Vehicle;

public interface RepoInterface {

    public void add(Vehicle a);

    public void remove(Vehicle a);

    public Vehicle[] getAll();

    public int getSize();

}
