package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.IExpression;
import Model.State.ProgState;
import Model.Values.Types.IType;

public class AssignmentStatement implements IStatement{
    String variableName;
    IExpression expression;

    public AssignmentStatement(String variableName, IExpression expression){
        this.variableName = variableName;
        this.expression = expression;
    }

    @Override
    public ProgState execute(ProgState state) throws AppException{
        state.getSymTable().setValue(this.variableName, this.expression.evaluate(state));
        return null;
    }

    @Override
    public String toString(){
        return this.variableName + " = " + this.expression.toString();
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        IType typeVar = typeEnv.LookUp(this.variableName);
        IType typexp = this.expression.typeCheck(typeEnv);
        if(typeVar.equals(typexp))
            return typeEnv;
        else
            throw new AppException("Assignement: right hand side and left hand side have different types.");
    }
}
