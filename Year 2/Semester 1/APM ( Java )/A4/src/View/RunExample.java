package View;

import Controller.Controller;
import Model.Exception.AppException;

public class RunExample extends Command{

    private Controller control;

    public RunExample(String key, String description, Controller control){
        super(key, description);
        this.control = control;
    }

    @Override
    public void execute(){
        try{
            this.control.executeAllSteps();
        } catch (AppException e) {
            System.out.println(e.getMessage());
        }
    }
}
