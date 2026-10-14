import java.util.*;

class hash {
    public List<List<Integer>> countFrequencies(int[] nums) {

        // Step 1: Create HashMap
        // Key = element
        // Value = frequency
        HashMap<Integer, Integer> map = new HashMap<>();

        // Step 2: Count frequency of each element
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // Step 3: Create the result list
        List<List<Integer>> result = new ArrayList<>();

        // Step 4: Iterate through all unique keys
        for (int key : map.keySet()) {

            // Create a pair [element, frequency]
            List<Integer> pair = new ArrayList<>();

            pair.add(key);
            pair.add(map.get(key));

            // Add the pair to result
            result.add(pair);
        }

        // Step 5: Return the result
        return result;
    }
}