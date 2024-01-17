package Controller;

import java.util.ArrayList;
import java.util.List;

import Controller.Interfaces.iGetModel;
import Controller.Interfaces.iGetView;
import Model.ModelClassList;
import Model.Core.Student;
import View.ViewClass;

public class ControllerClass {

    private iGetModel model;
    private iGetView view;
    private List<Student> studentBuffer = new ArrayList<>();

    public ControllerClass(iGetModel model, iGetView view) {
        this.model = model;
        this.view = view;
    }

    private boolean testData(List<Student> stud)
    {
        if(stud.size()>0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public void update()
    {

        //MVP
        studentBuffer = model.getStudents();

        if(testData(studentBuffer))
        {
            view.printAllStudents(studentBuffer);
        }
        else
        {
            System.out.println("Список студентов пуст!");
        }


        //MVC
        //view.printAllStudents(model.getStudents());
    } 
    
    public void run()
    {
        Command com = (Command)Command.NONE;
        boolean getNewIter = true;
        while(getNewIter)
        {
            String command = view.prompt("Введите команду:");
            com = Command.valueOf(command.toUpperCase());
            switch(com)
            {
                case EXIT:
                   getNewIter = false;
                   System.out.println("Выход из программы");
                   break;
                case LIST:
                   view.printAllStudents(model.getStudents());
                   break;
            }
        }
    }
}
