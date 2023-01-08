package View.GUI;

import Controller.IController;
import Model.Exception.AppException;
import View.GUI.MainWindow.MainWindowController;
import View.GUI.SetProgramWindow.SetProgramWindowController;
import View.IMainView;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class MainView extends Application implements IMainView {
    private static IController control;

    public static void setControl(IController control){
        MainView.control = control;
    }

    @Override
    public void start(Stage primaryStage){
        try{
            FXMLLoader mainWindowLoader = new FXMLLoader();
            mainWindowLoader.setLocation(getClass().getResource("MainWindow/MainWindow.fxml"));
            mainWindowLoader.setControllerFactory(c -> new MainWindowController(MainView.control));
            Parent mainWindowRoot = mainWindowLoader.load();
            MainWindowController mainWindowController = mainWindowLoader.getController();
            primaryStage.setTitle("Interpreter");
            primaryStage.setScene(new Scene(mainWindowRoot));
            primaryStage.show();

            Stage secondaryStage = new Stage();
            FXMLLoader setProgramLoader = new FXMLLoader();
            setProgramLoader.setControllerFactory(c -> new SetProgramWindowController(MainView.control, mainWindowController));
            setProgramLoader.setLocation(getClass().getResource("SetProgramWindow/SetProgramWindow.fxml"));
            Parent setProgramRoot = setProgramLoader.load();
            SetProgramWindowController setProgramWindowController = setProgramLoader.getController();
            secondaryStage.setTitle("Select program");
            secondaryStage.setScene(new Scene(setProgramRoot));
            secondaryStage.show();
        } catch(Exception exception){
            throw new RuntimeException(exception);
        }
    }

    @Override
    public void run(String[] args) throws AppException{
        launch(args);
    }

}
