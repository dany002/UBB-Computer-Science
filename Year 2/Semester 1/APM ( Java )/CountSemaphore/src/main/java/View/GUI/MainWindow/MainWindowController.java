package View.GUI.MainWindow;

import Controller.IController;
import Model.Exception.AppException;
import Model.State.*;
import Model.Statements.IStatement;
import Model.Values.IValue;
import javafx.fxml.FXML;

import javafx.beans.property.IntegerProperty;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.util.Callback;
import javafx.util.Pair;

import java.util.List;
import java.util.NoSuchElementException;

public class MainWindowController {
    IController controller;
    IHeap currentHeap;
    IOutput currentOutput;
    IFileTable currentFileTable;

    ISemaphoreTable currentSemaphoreTable;

    public MainWindowController(IController control){
        this.controller = control;
    }

    @FXML
    private Label programStateLabel;

    @FXML
    private ListView<Integer> programStateListView;

    @FXML
    private TableView<Pair<Integer, IValue>> heapTableTableView;

    @FXML
    private TableColumn<Pair<Integer, IValue>, Integer> heapAddressColumn;

    @FXML
    private TableColumn<Pair<Integer, IValue>, String> heapValueColumn;

    @FXML
    private ListView<String> outputListView;

    @FXML
    private ListView<String> fileTableListView;

    @FXML
    private TableView<Pair<String, IValue>> symbolTableTableView;

    @FXML
    private TableColumn<Pair<String, IValue>, String> symbolNameColumn;

    @FXML
    private TableColumn<Pair<String, IValue>, String> symbolValueColumn;

    @FXML
    private ListView<IStatement> executionStackListView;

    @FXML
    private Button stepButton;

    @FXML
    private Button runButton;

    @FXML
    private TableView<Pair<Integer,Pair<Integer,String>>> semaphoreTableTableView;

    @FXML
    private TableColumn<Pair<Integer,Pair<Integer,String>>,Integer> sempahoreIndexColumn;

    @FXML
    private TableColumn<Pair<Integer,Pair<Integer,String>>,Integer> semaphoreValueColumn;

    @FXML
    private TableColumn<Pair<Integer,Pair<Integer,String>>,String> semaphoreListOfValues;

    public void refresh(){
        Integer id = this.programStateListView.getSelectionModel().getSelectedItem();
        this.programStateListView.getItems().clear();
        this.heapTableTableView.getItems().clear();
        this.outputListView.getItems().clear();
        this.fileTableListView.getItems().clear();
        this.symbolTableTableView.getItems().clear();
        this.executionStackListView.getItems().clear();
        this.semaphoreTableTableView.getItems().clear();

        this.programStateLabel.setText("Program states: " + Integer.toString(this.controller.getProgStates().size()));
        this.controller.getProgStates().forEach(x -> this.programStateListView.getItems().add(x.getId()));

        if(this.controller.getProgStates().size() > 0){
            this.currentHeap = this.controller.getProgStates().get(0).getHeap();
            this.currentOutput = this.controller.getProgStates().get(0).getOutput();
            this.currentFileTable = this.controller.getProgStates().get(0).getFileTable();
        }
        if(this.currentHeap != null)
            this.currentHeap.toMap().forEach((x, y) -> this.heapTableTableView.getItems().add(new Pair<>(x, y)));

        if(this.currentOutput != null)
            this.currentOutput.getOutputAsList().forEach(x -> {
                this.outputListView.getItems().add(x);
            });

        if(this.currentFileTable != null)
            this.currentFileTable.getFileList().forEach(x -> {
                this.fileTableListView.getItems().add(x);
            });

        if(this.currentSemaphoreTable != null)
            this.currentSemaphoreTable.toMap().forEach((x, y) -> this.semaphoreTableTableView.getItems().add(new Pair<>(x, new Pair<>(y.getKey(),y.getValue().toString()))));

        ProgState currentProgram;
        try{
            currentProgram = this.controller.getProgStates().stream().filter(x -> Integer.valueOf(x.getId()).equals(id)).findAny().get();
            currentProgram.getSymTable().toMap().forEach((x, y) -> this.symbolTableTableView.getItems().add(new Pair<>(x, y)));
            List<IStatement> statementList = currentProgram.getExecutionStack().toList();
            for(int i = statementList.size() - 1; i >= 0; i--)
                this.executionStackListView.getItems().add(statementList.get(i));
        } catch(NoSuchElementException e){
            return ;
        } finally {
            this.programStateListView.refresh();
            this.heapTableTableView.refresh();
            this.executionStackListView.refresh();
            this.outputListView.refresh();
            this.symbolTableTableView.refresh();
            this.fileTableListView.refresh();
            this.semaphoreTableTableView.refresh();
        }
    }

    @FXML
    public void initialize(){
        this.heapAddressColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        this.heapValueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getValue().toString()));
        this.symbolNameColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getKey()));
        this.symbolValueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getValue().toString()));
        this.sempahoreIndexColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        this.semaphoreValueColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        this.semaphoreListOfValues.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getValue().toString()));
        this.refresh();
        this.runButton.setOnAction(actionEvent -> {
            try{
                this.controller.executeAllSteps();
            } catch(AppException | RuntimeException e){
                Alert alert = new Alert(Alert.AlertType.ERROR, e.toString(), ButtonType.OK);
                alert.showAndWait();
            } finally{
                this.refresh();
            }
        });

        this.stepButton.setOnAction(actionEvent -> {
            try{
                this.controller.executeOneStep();
            } catch(AppException | RuntimeException e){
                Alert alert = new Alert(Alert.AlertType.ERROR, e.toString(), ButtonType.OK);
                alert.showAndWait();
            } finally{
                this.refresh();
            }
        });
        this.programStateListView.setOnMouseClicked(x -> this.refresh());
    }

}
