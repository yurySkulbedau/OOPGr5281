

/**
 * Родительский класс
 */
public class Person<T,V> {
    // Поля
    private T name;
    private V age;

    /**
     * Конструктор
     * 
     * @param name // Имя
     * @param age  // Возраст
     */
    public Person(T name, V age) {
        this.name = name;
        this.age = age;
    }

    // Методы
    public T getName() {
        return name;
    }

    public void setName(T name) {
        this.name = name;
    }

    public V getAge() {
        return age;
    }

    public void setAge(V age) {
        this.age = age;
    }

    // Переопределение метода toString
    @Override
    public String toString() {
        return String.format("Имя = %s; Возраст = %d", getName(), getAge());
    }
}
