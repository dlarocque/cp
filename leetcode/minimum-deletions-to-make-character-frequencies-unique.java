class Solution {
    public int minDeletions(String s) {
        int[] freqs = new int[26]; // 26 possible characters and frequencies
        HashSet<Integer> usedFreq = new HashSet<Integer>();
        // generate the array of frequencies
        for(int i = 0; i < s.length(); i++) {
            ++freqs[s.charAt(i) - 'a'];
        }
        
        int deletions = 0;
        for(int i = 0; i < 26; i++) {
            // while the frequency of this character is not unique
            while(freqs[i] > 0 && !usedFreq.add(freqs[i])) {
                // delete the character (reduce frequency by one)
                --freqs[i];
                ++deletions;
            }
        }
        
        return deletions;
    }
}
