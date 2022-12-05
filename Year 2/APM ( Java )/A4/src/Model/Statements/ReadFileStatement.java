package Model.Statements;

import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.StringValue;
import Model.Values.Types.StringType;

public class ReadFileStatement implements IStatement{
    IExpression expression;
    String name;

    public ReadFileStatement(IExpression expression, String name){
        this.expression = expression;
        this.name = name;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException{
        IValue value = this.expression.evaluate(progState);
        if(!(value.getType() instanceof StringType))
            throw new AppException("Filename did not evaluate to string.");
        progState.getSymTable().setValue(name, new IntegerValue(progState.getFileTable().readFile(((StringValue) value).getValue())));
        return null;
    }

    @Override
    public String toString(){
        return "readFile(" + this.expression.toString() + ", " + this.name + ")";
    }
}
