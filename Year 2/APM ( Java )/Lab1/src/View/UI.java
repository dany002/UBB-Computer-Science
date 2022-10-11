package View;

import Controller.Controller;
import Model.Vehicle;

import javax.sound.midi.Soundbank;
import java.util.Scanner;

public class UI {

    private Controller control;

    public UI(Controller new_control){
        this.control = new_control;
        this.run_menu();
    }

    private void print_menu(){
        System.out.println("1. Add vehicle ");
        System.out.println("2. Remove vehicle ");
        System.out.println("3. Show all vehicles ");
        System.out.println("4. Show all vehicles with the repair cost greater than 1000 Ron ");
        System.out.println("5. Exit");
    }

    private void initial_list(){
        this.control.add("car", 100);
        this.control.add("motorcycle",1023);
        this.control.add("truck",3125);
        this.control.add("car",1243);
        this.control.add("motorcycle",123);
        this.control.add("truck",130);
        this.control.add("car",12415);
        this.control.add("motorcycle",1002);
        this.control.add("truck",1259);
    }

    private void add(){
        System.out.println("What do you want to add? Type: car, truck, motorcycle");
        String type;
        Scanner input = new Scanner(System.in);
        type = input.next();
        System.out.println("What is the cost of the repair?");
        int cost;
        try{
            cost = input.nextInt();
            this.control.add(type, cost);
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
    }

    private void remove(){
        System.out.println("What do you want to remove? Type: car, truck, motorcycle");
        String type;
        Scanner input = new Scanner(System.in);
        type = input.next();
        System.out.println("What is the cost of the repair?");
        int cost;
        try{
            cost = input.nextInt();
            this.control.remove(type, cost);
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
    }

    private void print_all(){
        Vehicle[] vehicles = this.control.getAll();
        for (int i = 0; i < this.control.getSize(); i++)
            System.out.println(vehicles[i].toString());
    }

    private void print_greater_than_1000(){
        Vehicle[] vehicles = this.control.getAll();
        for (int i = 0; i < this.control.getSize(); i++)
            if(vehicles[i].getCost() > 1000)
                System.out.println(vehicles[i].toString());
    }

    private void run_menu(){
        this.initial_list();
        String answer;
        int choice;
        Scanner input = new Scanner(System.in);
        while(true){
            this.print_menu();
            answer = input.next();
            try{
                choice = Integer.parseInt(answer);
            }
            catch (Exception e){
                System.out.println(e.getMessage());
                continue;
            }

            switch(choice){
                case 1:
                    this.add();
                    break;
                case 2:
                    this.remove();
                    break;
                case 3:
                    this.print_all();
                    break;
                case 4:
                    this.print_greater_than_1000();
                    break;
                case 5:
                    return;
                default:
                    System.out.println("Choose from 1-5!");
            }
        }
    }

}
