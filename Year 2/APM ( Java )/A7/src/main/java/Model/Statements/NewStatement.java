package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.IValue;
import Model.Values.RefValue;
import Model.Values.Types.IType;
import Model.Values.Types.RefType;

import java.sql.Ref;

public class NewStatement implements IStatement{

    String name;
    IExpression expression;

    public NewStatement(String name, IExpression expression){
        this.name = name;
        this.expression = expression;
    }

    @Override
    public ProgState execute(ProgState progState) throws AppException {
        IValue value = this.expression.evaluate(progState);
        progState.getSymTable().setValue(this.name, new RefValue(progState.getHeap().allocate(value), value.getType()));
        return null;
    }

    @Override
    public String toString(){
        return "new(" + this.name.toString() + ", " + this.expression.toString() + ")";
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        IType variableType = typeEnv.LookUp(this.name);
        IType expressionType = this.expression.typeCheck(typeEnv);
        if(variableType != null && variableType.equals(new RefType(expressionType)))
            return typeEnv;
        throw new AppException("Mismatched types for new statement.");
    }
}
