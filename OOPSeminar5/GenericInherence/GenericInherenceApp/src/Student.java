

/**
 * Дочерний класс для студента
 */
public class Student<T extends Comparable<T>,V> extends Person<T,V> implements Comparable<Student<T,V>> {
    // Поля
    private V id;
    //private V generalID;

    // Статическое поле для идентификатора студента
    // static {
    //     generalID = 0;
    // }

    /**
     * Конструктор
     * 
     * @param name // Имя
     * @param age  // Возраст
     */
    public Student(T name, V age) {
        super(name, age);
       // this.id = generalID;
        //generalID++;
    }

    // Методы
    public V getId() {
        return id;
    }

    // Переопределение метода toString
    @Override
    public String toString() {
        return super.toString() + String.format("; id = %s", getId());
    }

    // Переопределение метода compareTo
    @Override
    public int compareTo(Student<T,V> o) {

        return super.getName().compareTo(o.getName());
        // System.out.println(super.getName() + "-" + o.getName());
        // if (super.getAge() < o.getAge())
        //     return -1;
        // else if (super.getAge() > o.getAge())
        //     return 1;
        // if (this.getId() < o.getId())
        //     return -1;
        // else if (this.getId() > o.getId())
        //     return 1;
        // return 0;
    }
}
