class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> dupMap = new HashMap<>();

        for(int num : nums) {
            dupMap.put(num, dupMap.getOrDefault(num, 0) + 1);

            if(dupMap.get(num) > 1) {
                return true;
            }
        }

        return false;
    }
}
