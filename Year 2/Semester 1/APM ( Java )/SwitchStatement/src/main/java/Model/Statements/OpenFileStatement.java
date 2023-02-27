package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.StringValue;
import Model.Values.Types.IType;
import Model.Values.Types.StringType;

public class OpenFileStatement implements IStatement{
    IExpression expression;

    public OpenFileStatement(IExpression expression){
        this.expression = expression;
    }
    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue value = this.expression.evaluate(progState);
        if(!(value.getType() instanceof StringType)){
            throw new AppException("Filename did not evaluate to string.");
        }
        progState.getFileTable().openFile(((StringValue) value).getValue());
        return null;
    }

    @Override
    public String toString(){
        return "OpenRFile( " + this.expression.toString() + ")";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if((new StringType()).equals(this.expression.typeCheck(typeEnv)))
            return typeEnv;
        throw new AppException("Open file expression doesn't evaluate to a StringType.");
    }
}
