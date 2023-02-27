package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.Types.BooleanType;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;

public class NewLatchStatement implements IStatement{

    String name;
    IExpression expression;

    public NewLatchStatement(String name, IExpression expression){
        this.name = name;
        this.expression = expression;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue value = this.expression.evaluate(progState);
        int free_location = progState.getLatchTable().newLatch(((IntegerValue)value).getValue());
        try{
             IValue new_value = progState.getSymTable().getValue(this.name);
             progState.getSymTable().setValue(this.name,new IntegerValue(free_location));

        }
        catch(SymbolNotFoundAppException e){
            progState.getSymTable().declValue(this.name, new IntegerType());
            progState.getSymTable().setValue(this.name, new IntegerValue(free_location));
        }
        return null;
    }

    @Override
    public String toString(){
        return "newLatch(" + this.name + "," + this.expression.toString() + ");";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if((new IntegerType()).equals(this.expression.typeCheck(typeEnv)))
            return typeEnv;
        throw new AppException("Typecheck parameter has to evaluate to an integer.");
    }
}
