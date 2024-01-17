import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        //System.out.println("Hello, World!");

        Student<String,Integer> s1 = new Student<String,Integer>("Сергей", 25);
        System.out.println(s1);
        Student<String, Integer> s2 = new Student<String, Integer>("Андрей", 26);
        Student<String, Integer> s3 = new Student<String, Integer>("Даша", 23);

        List<Student<String, Integer>> listStud = new ArrayList<>();
        listStud.add(s1);
        listStud.add(s2);
        listStud.add(s3);

        StudentGroup<String,Integer> group = new StudentGroup<String,Integer>(55555, listStud);
        for(Student<String,Integer> stud: group)
        {
            System.out.println(stud);
        }
    }
}
