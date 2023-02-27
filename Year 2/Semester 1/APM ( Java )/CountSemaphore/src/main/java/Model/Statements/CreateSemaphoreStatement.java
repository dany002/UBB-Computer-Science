package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.Expressions.VariableExpression;
import Model.State.Exceptions.SymbolNotFoundAppException;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.IntegerValue;
import Model.Values.StringValue;
import Model.Values.Types.IType;
import Model.Values.Types.IntegerType;

public class CreateSemaphoreStatement implements IStatement{

    IExpression variable;
    IExpression number;

    public CreateSemaphoreStatement(IExpression variable, IExpression number){
        this.variable = variable;
        this.number = number;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue value = this.number.evaluate(progState);

        if(!(value.getType() instanceof IntegerType))
            throw new AppException("CreateSemaphoreStatement: Invalid expression, expression didn't evaluate to an integer.");

        IValue new_value = this.variable.evaluate(progState);

        if(!(new_value.getType() instanceof IntegerType))
            throw new AppException("CreateSemaphoreStatement: Invalid expression, var it's not an integer.");
        try {
            progState.getSymTable().getValue( this.variable.toString());
        }catch (SymbolNotFoundAppException e){
            throw new AppException("CreateSemaphoreStatement: Var not found in SymTable.");
        }
        int newFreeLocation = progState.getSemaphoreTable().createSemaphore(((IntegerValue) value).getValue());
        progState.getSymTable().setValue(this.variable.toString(), new IntegerValue(newFreeLocation));

        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        if(!(new IntegerType()).equals(this.variable.typeCheck(typeEnv)))
            throw new AppException("CreateSemaphoreStatement: The first argument is not int.");
        if(!(new IntegerType()).equals(this.number.typeCheck(typeEnv)))
            throw new AppException("CreateSemaphoreStatement: The second argument is not int.");
        return typeEnv;
    }

    @Override
    public String toString(){
        return "CreateSemaphore(" + this.variable.toString() + "," + this.number.toString() + ");";
    }
}
