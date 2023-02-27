package Model.State;

import Model.ADT.MyDictionary;
import Model.ADT.MyIDictionary;
import Model.Exception.ADTException;
import Model.Exception.AppException;
import Model.State.Exceptions.FileAlreadyOpenAppException;
import Model.State.Exceptions.FileNotOpenAppException;
import Model.State.Exceptions.InvalidFileFormatAppException;

import java.io.*;
import java.nio.channels.InterruptedByTimeoutException;
import java.nio.file.FileAlreadyExistsException;

public class FileTable implements IFileTable{
    MyIDictionary<String, BufferedReader> files;

    public FileTable(){
        this.files = new MyDictionary<>();
    }

    @Override
    public void openFile(String name) throws AppException {
        if(this.files.isVarDef(name))
            throw new FileAlreadyOpenAppException("File " + name + " already open for reading!");
        try{
            BufferedReader reader = new BufferedReader(new FileReader(name));
            this.files.put(name, reader);
        } catch(FileNotFoundException e){
            throw new AppException("Error opening file " + name);
        }
    }

    @Override
    public void closeFile(String name) throws AppException {
        try{
            this.files.removeKey(name);
        }
        catch(ADTException e){
            throw new FileNotOpenAppException("File " + name + " cannot be closed.");
        }
    }

    @Override
    public int readFile(String name) throws AppException {
        BufferedReader reader = null;
        try{
            reader = this.files.LookUp(name);
        }
        catch(ADTException e){
            throw new FileNotOpenAppException("File " + name + " cannot be read from.");
        }
        String data;
        try{
            data = reader.readLine();
        }
        catch(IOException e){
            throw new InvalidFileFormatAppException("Invalid line in file!");
        }

        if(data == null)
            data = "0";
        int answer = 0;
        try{
            answer = Integer.parseInt(data);
        }
        catch(NumberFormatException e){
            throw new InvalidFileFormatAppException("Invalid line in file");
        }
        return answer;
    }

    @Override
    public String toString(){
        StringBuilder ans = new StringBuilder();
        ans.append("Filetable: \n");
        for(String name : this.files.getKeys()){
            ans.append(name).append("\n");
        }
        return ans.toString();
    }

}



















