

import java.util.Iterator;
import java.util.List;

/**
 * Класс для группы студентов университета
 * Интерфейсы - Iterable для перебора списка студентов групп и Comparable для
 * сортировки групп
 */
public class StudentGroup<T extends Comparable<T>,V> implements Iterable<Student<T,V>>, Comparable<StudentGroup<T,V>> {
    // Поля
    private V numberGroup; // Номер группы
    List<Student<T,V>> students; // Список студентов группы

    /**
     * Конструктор
     * 
     * @param numberGroup // Номер группы
     * @param students    // Список студентов группы
     */
    public StudentGroup(V numberGroup, List<Student<T,V>> students) {
        this.numberGroup = numberGroup;
        this.students = students;
    }

    // Методы
    public V getNumberGroup() {
        return numberGroup;
    }

    public void setNumberGroup(V numberGroup) {
        this.numberGroup = numberGroup;
    }

    /**
     * @return Возвращает значение количества учащихся в группе
     */
    public int getSizeStudentGroup() {
        return students.size();
    }

    @Override
    public String toString() {
        StringBuilder list = new StringBuilder();
        list.append(String.format("Номер группы - %d, Количество студентов - %d; Список студентов:\n",
                getNumberGroup(), getSizeStudentGroup()));
        for (Student<T,V> student : students) {
            list.append(student).append("\n");
        }
        return list.toString();
    }

    // Доступ к списку сдудентов в группе
    @Override
    public Iterator<Student<T,V>> iterator() {
        return new StudentIterator<T,V>(students);
    }

    // Переопредление метода CompareTo
    @Override
    public int compareTo(StudentGroup<T,V> o) {
        if (getSizeStudentGroup() < o.getSizeStudentGroup()) {
            return -1;
        } else if (getSizeStudentGroup() > o.getSizeStudentGroup()) {
            return 1;
        }
        // if (getNumberGroup() < o.getNumberGroup()) {
        //     return -1;
        // } else if (getNumberGroup() > o.getNumberGroup()) {
        //     return 1;
        // }
        return 0;
    }
}
