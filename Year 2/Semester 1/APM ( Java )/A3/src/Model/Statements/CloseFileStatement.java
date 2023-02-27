package Model.Statements;

import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.StringValue;
import Model.Values.Types.StringType;

public class CloseFileStatement implements IStatement{
    IExpression expression;

    public CloseFileStatement(IExpression expression){
        this.expression = expression;
    }

    @Override
    public void execute(ProgState progState) throws AppException{
        IValue value = this.expression.evaluate(progState);
        if(!(value.getType() instanceof StringType))
            throw new AppException("Filename did not evaluate to string");
        progState.getFileTable().closeFile(((StringValue) value).getValue());
    }

    @Override
    public String toString(){
        return "CloseRFile(" + this.expression.toString() + ")";
    }

}
