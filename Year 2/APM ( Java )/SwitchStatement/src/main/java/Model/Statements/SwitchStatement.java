package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IType;

public class SwitchStatement implements IStatement{

    IExpression expression;

    IExpression condition_one;

    IExpression condition_two;

    IStatement first_statement;

    IStatement second_statement;

    IStatement default_statement;

    public SwitchStatement(IExpression expression, IExpression condition_one, IStatement first_statement, IExpression condition_two, IStatement second_statement, IStatement default_statement){
        this.expression = expression;
        this.condition_one = condition_one;
        this.first_statement = first_statement;
        this.condition_two = condition_two;
        this.second_statement = second_statement;
        this.default_statement = default_statement;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue first_value = this.expression.evaluate(progState);

        IValue second_value = this.condition_one.evaluate(progState);

        IValue third_value = this.condition_two.evaluate(progState);


        if(first_value.equals(second_value))
            progState.getExecutionStack().push(this.first_statement);
        else if(first_value.equals(third_value))
            progState.getExecutionStack().push(this.second_statement);
        else
            progState.getExecutionStack().push(this.default_statement);

        return null;
    }

    @Override
    public String toString(){
        return "Switch(" + this.expression.toString() + ")\n\t(case (" + this.condition_one.toString() + ")" + this.first_statement.toString() + ")\n\t(case (" + this.condition_two.toString() + ")" + this.second_statement.toString() + ")\n\t" + this.default_statement.toString() + '\n';
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {

        this.first_statement.typeCheck(typeEnv.copy());
        this.second_statement.typeCheck(typeEnv.copy());
        this.default_statement.typeCheck(typeEnv.copy());
        return typeEnv;
    }
}
