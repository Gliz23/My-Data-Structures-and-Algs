

public class Arrays {
    public static void main(String[] args) {
        Array numbers = new Array(3);
        numbers.insert(10);
        numbers.insert(20);
        numbers.insert(30);
        numbers.insert(40);
        numbers.removeAt(2);
        numbers.print();
    }

    public class delete {
        //An array of numbers is created.
        private int[] numbers;

        private int size;

        //Items of any length is converted into an array and stored in numbers.
        public delete(int length) {
            numbers = new int[length];
        }


        public void removeAt(int index) {
            //If an index is provided outside the range of indexes, an error message will show.
            if (index < 0 || index >= size)
                throw new IllegalArgumentException();

            //In order to delete a number we can just shift numbers backward.
            for (int i = index; i < size; i++)
                numbers[i] = numbers[i + 1];

            //...and delete the last number in the array.
            size--;

        }
    }




}






