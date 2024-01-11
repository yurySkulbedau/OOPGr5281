

import java.util.Iterator;
import java.util.List;

/**
 * Класс для перебора студентов в группах
 */
public class StudentIterator<T extends Comparable<T>,V> implements Iterator<Student<T,V>> {
    // Поля
    private int count;
    private List<Student<T,V>> students;

    /**
     * 
     * @param students // Студенты в группе
     */
    public StudentIterator(List<Student<T,V>> students) {
        this.students = students;
        count = 0;
    }

    // Методы
    @Override
    public boolean hasNext() {
        return count < students.size();
    }

    @Override
    public Student<T,V> next() {
        return students.get(count++);
    }

}
