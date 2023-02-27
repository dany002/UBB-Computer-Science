import Controller.Controller;
import Model.Expressions.BinaryExpression;
import Model.Expressions.ConstantExpression;
import Model.Expressions.VariableExpression;
import Model.State.*;
import Model.Statements.*;
import Model.Values.BooleanValue;
import Model.Values.IntegerValue;
import Model.Values.StringValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IntegerType;
import Model.Values.Types.StringType;
import Repository.IRepository;
import Repository.Repository;
import View.TextMenu;
import View.ExitCommand;
import View.RunExample;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        IStatement ex1 = new CompositeStatement(
                            new VariableDeclarationStatement("v",new IntegerType()),
                            new CompositeStatement(
                                    new AssignmentStatement(
                                            "v",
                                            new ConstantExpression(new IntegerValue(2))),
                                    new PrintStatement(
                                            new VariableExpression("v"))
                            )
        );
        List<ProgState> prg1 = new ArrayList<>();
        prg1.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), ex1));
        IRepository repo1 = new Repository(prg1,"log1.txt");
        Controller ctrl1 = new Controller(repo1, true);

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
        prg2.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), ex2));
        IRepository repo2 = new Repository(prg2,"log2.txt");
        Controller ctrl2 = new Controller(repo2, true);

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
        prg3.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), ex3));
        IRepository repo3 = new Repository(prg3,"log3.txt");
        Controller ctrl3 = new Controller(repo3, true);

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
        prg4.add(new ProgState(new ExecutionStack(), new SymTable(), new Output(), new FileTable(), ex4));
        IRepository repo4 = new Repository(prg4,"log4.txt");
        Controller ctrl4 = new Controller(repo4, true);

        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));
        menu.addCommand(new RunExample("1", ex1.toString(), ctrl1));
        menu.addCommand(new RunExample("2", ex2.toString(), ctrl2));
        menu.addCommand(new RunExample("3", ex3.toString(), ctrl3));
        menu.addCommand(new RunExample("4", ex4.toString(), ctrl4));
        menu.show();
    }
}












