package View.GUI.SetProgramWindow;

import Controller.IController;
import Model.Exception.AppException;
import Model.Expressions.BinaryExpression;
import Model.Expressions.ConstantExpression;
import Model.Expressions.ReadHeapExpression;
import Model.Expressions.VariableExpression;
import Model.Statements.*;
import Model.Values.BooleanValue;
import Model.Values.IntegerValue;
import Model.Values.StringValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IntegerType;
import Model.Values.Types.RefType;
import Model.Values.Types.StringType;
import View.GUI.MainWindow.MainWindowController;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.scene.control.TextArea;

import java.util.ArrayList;
import java.util.List;

public class SetProgramWindowController {
    MainWindowController siblingController;
    IController control;

    @FXML
    private TextArea error;

    @FXML
    private ListView<IStatement> programsListView;

    @FXML
    private Button setProgramButton;

    public SetProgramWindowController(IController control, MainWindowController siblingController){
        this.control = control;
        this.siblingController = siblingController;
    }

    @FXML
    public void initialize(){
        List<IStatement> hardcodedPrograms = new ArrayList<IStatement>(List.of(
                new CompositeStatement(new VariableDeclarationStatement("v",new IntegerType()), new CompositeStatement(new AssignmentStatement("v",new ConstantExpression(new BooleanValue(true))), new PrintStatement(new VariableExpression("v")))),
                new CompositeStatement(new VariableDeclarationStatement("a",new IntegerType()), new CompositeStatement(new AssignmentStatement("a",new BinaryExpression(new ConstantExpression(new IntegerValue(2)),new BinaryExpression(new ConstantExpression(new IntegerValue(3)),new ConstantExpression(new IntegerValue(5)),"*"),"+")), new CompositeStatement(new VariableDeclarationStatement("b",new IntegerType()), new CompositeStatement(new AssignmentStatement("b",new BinaryExpression(new BinaryExpression(new VariableExpression("a"),new BinaryExpression(new ConstantExpression(new IntegerValue(4)),new ConstantExpression(new IntegerValue(2)),"/"),"-"),new ConstantExpression(new IntegerValue(7)),"+")), new PrintStatement(new VariableExpression("b")))))),
                new CompositeStatement(new VariableDeclarationStatement("a",new BooleanType()), new CompositeStatement(new AssignmentStatement("a",new ConstantExpression(new BooleanValue(false))), new CompositeStatement(new VariableDeclarationStatement("v",new IntegerType()), new IfStatement(new VariableExpression("a"), new AssignmentStatement("v",new ConstantExpression(new IntegerValue(2))), new AssignmentStatement("v",new ConstantExpression(new IntegerValue(3))))))),
                new CompositeStatement(new VariableDeclarationStatement("varf",new StringType()), new CompositeStatement(new AssignmentStatement("varf",new ConstantExpression(new StringValue("test.txt"))), new CompositeStatement(new OpenFileStatement(new VariableExpression("varf")), new CompositeStatement(new VariableDeclarationStatement("varc",new IntegerType()), new CompositeStatement(new ReadFileStatement(new VariableExpression("varf"), "varc"), new CompositeStatement(new PrintStatement(new VariableExpression("varc")), new CompositeStatement(new ReadFileStatement(new VariableExpression("varf"), "varc"), new CompositeStatement(new PrintStatement(new VariableExpression("varc")), new CloseFileStatement(new VariableExpression("varf")))))))))),
                new CompositeStatement(new VariableDeclarationStatement("v",new RefType(new IntegerType())), new CompositeStatement(new NewStatement("v", new ConstantExpression(new IntegerValue(20))), new CompositeStatement(new VariableDeclarationStatement("a",new RefType(new RefType(new IntegerType()))), new CompositeStatement(new NewStatement("a", new VariableExpression("v")), new CompositeStatement(new PrintStatement(new VariableExpression("v")), new PrintStatement(new VariableExpression("a"))))))),
                new CompositeStatement(new VariableDeclarationStatement("v",new RefType(new IntegerType())), new CompositeStatement(new NewStatement("v", new ConstantExpression(new IntegerValue(20))), new CompositeStatement(new VariableDeclarationStatement("a",new RefType(new RefType(new IntegerType()))), new CompositeStatement(new NewStatement("a", new VariableExpression("v")), new CompositeStatement(new PrintStatement(new ReadHeapExpression(new VariableExpression("v"))), new PrintStatement(new BinaryExpression(new ReadHeapExpression(new ReadHeapExpression(new VariableExpression("a"))),new ConstantExpression(new IntegerValue(5)),"+"))))))),
                new CompositeStatement(new VariableDeclarationStatement("v",new RefType(new IntegerType())), new CompositeStatement(new NewStatement("v", new ConstantExpression(new IntegerValue(20))), new CompositeStatement(new PrintStatement(new ReadHeapExpression(new VariableExpression("v"))), new CompositeStatement(new WriteHeapStatement(new VariableExpression("v"), new ConstantExpression(new IntegerValue(30))), new PrintStatement(new BinaryExpression(new ReadHeapExpression(new VariableExpression("v")),new ConstantExpression(new IntegerValue(5)),"+")))))),
                new CompositeStatement(new VariableDeclarationStatement("v",new RefType(new IntegerType())), new CompositeStatement(new NewStatement("v", new ConstantExpression(new IntegerValue(20))), new CompositeStatement(new VariableDeclarationStatement("a",new RefType(new RefType(new IntegerType()))), new CompositeStatement(new NewStatement("a", new VariableExpression("v")), new CompositeStatement(new NewStatement("v", new ConstantExpression(new IntegerValue(30))), new PrintStatement(new ReadHeapExpression(new ReadHeapExpression(new VariableExpression("a"))))))))),
                new CompositeStatement(new VariableDeclarationStatement("v",new IntegerType()), new CompositeStatement(new AssignmentStatement("v",new ConstantExpression(new IntegerValue(4))), new CompositeStatement(new WhileStatement(new BinaryExpression(new VariableExpression("v"),new ConstantExpression(new IntegerValue(0)),">"), new CompositeStatement(new PrintStatement(new VariableExpression("v")), new AssignmentStatement("v",new BinaryExpression(new VariableExpression("v"),new ConstantExpression(new IntegerValue(1)),"-")))), new PrintStatement(new VariableExpression("v"))))),
                new CompositeStatement(new VariableDeclarationStatement("v",new IntegerType()), new CompositeStatement(new VariableDeclarationStatement("a",new RefType(new IntegerType())), new CompositeStatement(new AssignmentStatement("v",new ConstantExpression(new IntegerValue(10))), new CompositeStatement(new NewStatement("a", new ConstantExpression(new IntegerValue(22))), new CompositeStatement(new ForkStatement(new CompositeStatement(new WriteHeapStatement(new VariableExpression("a"), new ConstantExpression(new IntegerValue(30))), new CompositeStatement(new AssignmentStatement("v",new ConstantExpression(new IntegerValue(32))), new CompositeStatement(new PrintStatement(new VariableExpression("v")), new PrintStatement(new ReadHeapExpression(new VariableExpression("a"))))))), new CompositeStatement(new PrintStatement(new VariableExpression("v")), new PrintStatement(new ReadHeapExpression(new VariableExpression("a")))))))))
        ));
        this.programsListView.setItems(FXCollections.observableList(hardcodedPrograms));
        setProgramButton.setOnAction(actionEvent -> {
            try{
                int index = this.programsListView.getSelectionModel().getSelectedIndex();
                if(index < 0)
                    throw new AppException("No index selected!");
                else if(index >= hardcodedPrograms.size())
                    throw new AppException("No program at selected index!");
                this.control.setProgram(hardcodedPrograms.get(index));
            }
            catch (AppException e){
                this.error.setText("Error: " + e.toString());
                this.error.setStyle("-fx-text-fill: red");
            } finally {
                this.siblingController.refresh();
            }
        });
    }

}
