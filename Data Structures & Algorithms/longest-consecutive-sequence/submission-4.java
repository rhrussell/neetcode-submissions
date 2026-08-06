class Solution {
    public int longestConsecutive(int[] nums) {
        int temp = 0;
        int result = 1;

        TreeSet<Integer> sortedSet = new TreeSet<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        if(nums.length > 0)
        {
            for(int num : nums) 
            {
                sortedSet.add(num);
            }

            temp = sortedSet.pollFirst();

            for(Integer element : sortedSet)
            {
                if(temp + 1 == element)
                {
                    result += 1;
                }
                else
                {
                    maxHeap.add(result);
                    result = 1;
                }

                temp = element;
            }

            maxHeap.add(result);

            result = maxHeap.peek();
        }
        else
        {
            result = 0;
        }

        return result;
    }
}
