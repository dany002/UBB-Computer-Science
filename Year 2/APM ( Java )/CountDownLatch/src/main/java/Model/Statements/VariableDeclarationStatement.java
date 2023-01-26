package Model.Statements;

import Model.ADT.MyIDictionary;
import Model.Exception.AppException;
import Model.Expressions.VariableExpression;
import Model.State.ProgState;
import Model.Values.Types.IType;

public class VariableDeclarationStatement implements IStatement{
    String name;
    IType type;

    public VariableDeclarationStatement(String name, IType type){
        this.name = name;
        this.type = type;
    }

    @Override
    public ProgState execute(ProgState state) throws AppException{
        state.getSymTable().declValue(this.name, this.type);
        return null;
    }

    @Override
    public String toString(){
        return this.type.toString() + " " + this.name;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnv) throws AppException {
        typeEnv.put(this.name, this.type);
        return typeEnv;
    }
}
