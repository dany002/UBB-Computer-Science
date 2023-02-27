import Controller.Controller;
import Repository.Repository;
import View.UI;

public class Main {
    public static void main(String[] args) {
        Repository repo = new Repository();
        Controller control = new Controller(repo);
        UI ui = new UI(control);
    }
}