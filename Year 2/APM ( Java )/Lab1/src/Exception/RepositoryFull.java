package Exception;

public class RepositoryFull extends RuntimeException{
    public RepositoryFull(){
        super("You can't add another vehicle because the repository is full.");
    }

    public RepositoryFull(String message){
        super(message);
    }
}
