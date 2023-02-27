import Controller.Controller;
import Model.Expressions.BinaryExpression;
import Model.Expressions.ConstantExpression;
import Model.Expressions.ReadHeapExpression;
import Model.Expressions.VariableExpression;
import Model.State.*;
import Model.Statements.*;
import Model.Values.BooleanValue;
import Model.Values.IntegerValue;
import Model.Values.StringValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IntegerType;
import Model.Values.Types.RefType;
import Model.Values.Types.StringType;
import Repository.IRepository;
import Repository.Repository;
import View.TextMenu;
import View.ExitCommand;
import View.RunExample;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        IStatement ex1 = new CompositeStatement(
                            new VariableDeclarationStatement("v",new IntegerType()),
                            new CompositeStatement(
                                    new AssignmentStatement(
                                            "v",
                                            new ConstantExpression(new BooleanValue(true))),
                                    new PrintStatement(
                                            new VariableExpression("v"))
                            )
        );
        List<ProgState> prg1 = new ArrayList<>();
        prg1.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), new Heap(), ex1));
        IRepository repo1 = new Repository(prg1,"log1.txt");
        Controller ctrl1 = new Controller(repo1, Executors.newFixedThreadPool(2), true);
        IStatement ex2 = new CompositeStatement(
                            new VariableDeclarationStatement("a",new IntegerType()),
                            new CompositeStatement(
                                new VariableDeclarationStatement("b",new IntegerType()),
                                new CompositeStatement(
                                        new AssignmentStatement(
                                                "a",
                                                new BinaryExpression(
                                                        new ConstantExpression(
                                                                new IntegerValue(2)),
                                                    new BinaryExpression(
                                                            new ConstantExpression(new IntegerValue(3)),
                                        new ConstantExpression(new IntegerValue(5)),
                                                            "*"),
                                                        "+")
                                        ),
                                    new CompositeStatement(
                                        new AssignmentStatement(
                                                "b",
                                                new BinaryExpression(
                                                        new VariableExpression("a"),
                                                new ConstantExpression(new IntegerValue(1)),
                                                        "+")),
                                        new PrintStatement(new VariableExpression("b"))
                                    )
                                )
                            )
        );

        List<ProgState> prg2 = new ArrayList<>();
        prg2.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), new Heap(), ex2));
        IRepository repo2 = new Repository(prg2,"log2.txt");
        Controller ctrl2 = new Controller(repo2, Executors.newFixedThreadPool(2), true);

        IStatement ex3 = new CompositeStatement(
                            new VariableDeclarationStatement(
                                "a",
                                    new BooleanType()),
                                    new CompositeStatement(
                                        new VariableDeclarationStatement(
                                                "v",
                                                new IntegerType()
                                        ),
                                            new CompositeStatement(
                                                    new AssignmentStatement(
                                                            "a",
                                                            new ConstantExpression(new BooleanValue(true))
                                                    ),
                                                    new CompositeStatement(
                                                            new IfStatement(
                                                                    new VariableExpression("a"),
                                                                    new AssignmentStatement(
                                                                            "v",
                                                                            new ConstantExpression(new IntegerValue(2))
                                                                    ),
                                                                    new AssignmentStatement(
                                                            "v",
                                                                            new ConstantExpression(new IntegerValue(3))
                                                                    )
                                                            ),
                                                            new PrintStatement(new VariableExpression("v"))
                                                    )
                                            )
                                    )
        );

        List<ProgState> prg3 = new ArrayList<>();
        prg3.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), new Heap(), ex3));
        IRepository repo3 = new Repository(prg3,"log3.txt");
        Controller ctrl3 = new Controller(repo3, Executors.newFixedThreadPool(2), true);

        /*
        string varf;varf="test.in";openRFile(varf);int varc;readFile(varf,varc);print(varc); readFile(varf,varc);print(varc)   closeRFile(varf)

         */
        IStatement ex4 = new CompositeStatement(
                new VariableDeclarationStatement(
                        "varf",
                        new StringType()
                ),
                new CompositeStatement(
                        new AssignmentStatement(
                                "varf",
                                new ConstantExpression(
                                        new StringValue("test.in")
                                )
                        ),
                        new CompositeStatement(
                            new OpenFileStatement(
                                new VariableExpression("varf")
                            ), new CompositeStatement(
                                    new VariableDeclarationStatement("varc", new StringType()),
                                    new CompositeStatement(
                                        new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                            new CompositeStatement(
                                            new PrintStatement(new VariableExpression("varc")),
                                                new CompositeStatement(
                                new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                                        new CompositeStatement(
                                                                new PrintStatement(new VariableExpression("varc")),
                                                                new CloseFileStatement(new VariableExpression("varf"))
                                                        )
                                                )
                                            )
                                    )
                        )
                        )
                )
        );

        List<ProgState> prg4 = new ArrayList<>();
        prg4.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), new Heap(), ex4));
        IRepository repo4 = new Repository(prg4,"log4.txt");
        Controller ctrl4 = new Controller(repo4, Executors.newFixedThreadPool(2), true);


        IStatement ex5 = new CompositeStatement(new VariableDeclarationStatement("v", new RefType(new IntegerType())),
                new CompositeStatement(new NewStatement("v", new ConstantExpression(new IntegerValue(20))),
                        new CompositeStatement(new VariableDeclarationStatement("a", new RefType(new RefType(new IntegerType()))),
                                new CompositeStatement(new NewStatement("a", new VariableExpression("v")),
                                        new CompositeStatement(new PrintStatement(new VariableExpression("v")), new PrintStatement(new VariableExpression("a")))))));
        List<ProgState> prg5 = new ArrayList<>();
        prg5.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), new Heap(), ex5));
        IRepository repo5 = new Repository(prg5, "log5.txt");
        Controller ctrl5 = new Controller(repo5, Executors.newFixedThreadPool(2), true);

        IStatement ex6 = new CompositeStatement(new VariableDeclarationStatement("v", new RefType(new IntegerType())),
                new CompositeStatement(new NewStatement("v", new ConstantExpression(new IntegerValue(20))),
                        new CompositeStatement(new VariableDeclarationStatement("a", new RefType(new RefType(new IntegerType()))),
                                new CompositeStatement(new NewStatement("a", new VariableExpression("v")),
                                        new CompositeStatement(new PrintStatement(new ReadHeapExpression(new VariableExpression("v"))),
                                                new PrintStatement(new BinaryExpression(new ReadHeapExpression(new ReadHeapExpression(new VariableExpression("a"))), new ConstantExpression(new IntegerValue(5)), "+")))))));

        List<ProgState> prg6 = new ArrayList<>();
        prg6.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), new Heap(), ex6));
        IRepository repo6 = new Repository(prg6, "log6.txt");
        Controller ctrl6 = new Controller(repo6, Executors.newFixedThreadPool(2), true);


        IStatement ex7 =  new CompositeStatement(new VariableDeclarationStatement("v", new RefType(new IntegerType())),
                new CompositeStatement(new NewStatement("v", new ConstantExpression(new IntegerValue(20))),
                        new CompositeStatement(new VariableDeclarationStatement("a", new RefType(new RefType(new IntegerType()))),
                                new CompositeStatement(new NewStatement("a", new VariableExpression("v")),
                                        new CompositeStatement(new NewStatement("v", new ConstantExpression(new IntegerValue(30))),
                                                new PrintStatement(new ReadHeapExpression(new ReadHeapExpression(new VariableExpression("a")))))))));

        List<ProgState> prg7 = new ArrayList<>();
        prg7.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), new Heap(), ex7));
        IRepository repo7 = new Repository(prg7, "log6.txt");
        Controller ctrl7 = new Controller(repo7, Executors.newFixedThreadPool(2), true);

        IStatement ex8 = new CompositeStatement(new VariableDeclarationStatement("v", new IntegerType()),
                new CompositeStatement(new AssignmentStatement("v", new ConstantExpression(new IntegerValue(4))),
                        new CompositeStatement(new WhileStatement(new BinaryExpression( new VariableExpression("v"), new ConstantExpression(new IntegerValue(0)), ">"),
                                new CompositeStatement(new PrintStatement(new VariableExpression("v")), new AssignmentStatement("v",new BinaryExpression(new VariableExpression("v"), new ConstantExpression(new IntegerValue(1)), "-")))),
                                new PrintStatement(new VariableExpression("v")))));



        List<ProgState> prg8 = new ArrayList<>();
        prg8.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), new Heap(), ex8));
        IRepository repo8 = new Repository(prg8, "log8.txt");
        Controller ctrl8 = new Controller(repo8, Executors.newFixedThreadPool(2), true);

        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));
        menu.addCommand(new RunExample("1", ex1.toString(), ctrl1));
        menu.addCommand(new RunExample("2", ex2.toString(), ctrl2));
        menu.addCommand(new RunExample("3", ex3.toString(), ctrl3));
        menu.addCommand(new RunExample("4", ex4.toString(), ctrl4));
        menu.addCommand(new RunExample("5", ex5.toString(), ctrl5));
        menu.addCommand(new RunExample("6", ex6.toString(), ctrl6));
        menu.addCommand(new RunExample("7", ex7.toString(), ctrl7));
        menu.addCommand(new RunExample("8", ex8.toString(), ctrl8));
        menu.show();
    }
}












