import Controller.Controller;
import Model.Expressions.BinaryExpression;
import Model.Expressions.ConstantExpression;
import Model.Expressions.VariableExpression;
import Model.Statements.*;
import Model.Values.BooleanValue;
import Model.Values.IntegerValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IntegerType;
import View.View;

import java.util.ArrayList;

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

        Controller ctrl1 = new Controller(ex1);

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

        Controller ctrl2 = new Controller(ex2);

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
        ArrayList<IStatement> list_with_statements = new ArrayList<IStatement>();
        list_with_statements.add(ex1);
        list_with_statements.add(ex2);
        list_with_statements.add(ex3);
        Controller ctrl3 = new Controller(ex3);
        View view = new View(list_with_statements);
        view.run();
    }
}












