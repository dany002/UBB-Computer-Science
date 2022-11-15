package View;

import Controller.Controller;
import Model.Exception.AppException;
import Model.Statements.IStatement;

import java.util.ArrayList;
import java.util.Objects;
import java.util.Scanner;

public class View implements IView{

    Controller control;
    ArrayList<IStatement> list_with_statements;

    public View(ArrayList<IStatement> list_with_statements){
        this.list_with_statements = list_with_statements;
    }

    public void help(){
        System.out.println("-1 for exit");
        System.out.println("1 for one step");
        System.out.println("2 for all steps");
    }

    public void onestep() throws AppException {
        this.control.executeOneStep();
    }

    public void allsteps() throws AppException{
        this.control.executeAllSteps();
    }

    public void chooseProgram(){
        System.out.println("Choose between program 1-3");
        int choice = 0;
        String answer;
        Scanner input = new Scanner(System.in);
        answer = input.next();
        try{
            choice = Integer.parseInt(answer);
        }
        catch (Exception e){
            System.out.println(e.getMessage());
            this.chooseProgram();
        }

        switch (choice) {
            case 1 -> this.control = new Controller(this.list_with_statements.get(0));
            case 2 -> this.control = new Controller(this.list_with_statements.get(1));
            case 3 -> this.control = new Controller(this.list_with_statements.get(2));
            default -> {
                System.out.println("Fail");
                this.chooseProgram();
            }
        }
    }

    @Override
    public void run(){
        this.chooseProgram();
        int choice;
        String answer;
        Scanner input = new Scanner(System.in);
        System.out.println("Do u want to display or not?");
        answer = input.next();
        this.control.setDisplayFlag(Objects.equals(answer, "yes"));
        while(true) {
            this.help();
            answer = input.next();

            try {
                choice = Integer.parseInt(answer);
            } catch (Exception e) {
                System.out.println(e.getMessage());
                continue;
            }
            try {
                switch (choice) {
                    case 1:
                        this.onestep();
                        break;
                    case 2:
                        this.allsteps();
                        break;
                    case -1:
                        return;
                    default:
                        System.out.println("Choose from -1,1,2");
                }
            } catch (AppException exception) {
                System.out.println(exception.getMessage());
            }
        }
    }
}
