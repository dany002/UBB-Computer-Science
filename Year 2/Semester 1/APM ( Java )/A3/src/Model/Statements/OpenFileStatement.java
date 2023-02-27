package Model.Statements;

import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.StringValue;
import Model.Values.Types.StringType;

public class OpenFileStatement implements IStatement{
    IExpression expression;

    public OpenFileStatement(IExpression expression){
        this.expression = expression;
    }
    @Override
    public void execute(ProgState progState) throws AppException {
        IValue value = this.expression.evaluate(progState);
        if(!(value.getType() instanceof StringType)){
            throw new AppException("Filename did not evaluate to string.");
        }
        progState.getFileTable().openFile(((StringValue) value).getValue());
    }

    @Override
    public String toString(){
        return "OpenRFile( " + this.expression.toString() + ")";
    }
}
