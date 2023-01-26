import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {

        List<Integer> numbers = Arrays.asList(1,2,3,4,5,6,7,8,9,10,11,12,14,15);
        System.out.println(numbers.stream().filter(p -> p % 5 == 0 || p % 2 == 0).map(a -> "N" + Integer.toString(a) + "R").collect(Collectors.joining()));
        //
        System.out.println(Arrays.asList(numbers.stream().filter(p -> p % 4 == 0).map(t -> t + 1).reduce(0, (a,b) -> (a+b) % 2)));

        //lecture
        List<String> myList = Arrays.asList("a1", "a2", "b1", "c2", "c1");
        myList.stream().map(String::toUpperCase).sorted().forEach(System.out::println);
    }
}