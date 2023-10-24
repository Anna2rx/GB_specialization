import java.io.FileWriter;
import java.io.IOException;
import java.util.PriorityQueue;

public class ToyStore {
    private static final int NUM_TRIALS = 10;
    private static final int ARRAYS_COUNT = 3;
    private PriorityQueue<Toy> toys;

    public ToyStore() {
        toys = new PriorityQueue<>();
    }

    public void put(String id, String name, int weight) {
        Toy toy = new Toy(id, name, weight);
        toys.add(toy);
    }

    public String get() {
        int randomNum = (int) (Math.random() * 100) + 1;
        
        if (randomNum <= 20) {
            return "1";
        } else if (randomNum <= 40) {
            return "2";
        } else {
            return "3";
        }
    }

    public void run() {
        try {
            FileWriter fileWriter = new FileWriter("output.txt");
            for (int j = 0; j < ARRAYS_COUNT; j++) {
                String[] ids = new String[NUM_TRIALS];
                for (int i = 0; i < NUM_TRIALS; i++) {
                    String result = get();
                    ids[i] = result;
                    fileWriter.write(ids[i] + "\n");
                }
            }
            fileWriter.close();
            System.out.println("Результаты записаны в файл output.txt");

        } catch (IOException e) {
            System.out.println("Ошибка при записи в файл");
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        ToyStore toyStore = new ToyStore();
        toyStore.put("1", "конструктор", 2);
        toyStore.put("2", "робот", 2);
        toyStore.put("3", "кукла", 6);
        toyStore.run();
    }
}

class Toy implements Comparable<Toy> {
    private String id;
    private String name;
    private int weight;

    public Toy(String id, String name, int weight) {
        this.id = id;
        this.name = name;
        this.weight = weight;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getWeight() {
        return weight;
    }

    @Override
    public int compareTo(Toy other) {
        return Integer.compare(this.weight, other.weight);
    }
}