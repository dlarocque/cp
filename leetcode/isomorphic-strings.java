class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Integer> smap = new HashMap<>();
        HashMap<Character, Integer> tmap = new HashMap<>();

        for(int i = 0; i < s.length(); i++) {
            if(smap.get(s.charAt(i)) == null) {
                smap.put(s.charAt(i), i);
            }
            if(tmap.get(t.charAt(i)) == null) {
                tmap.put(t.charAt(i), i);
            }

            if(smap.get(s.charAt(i)) != tmap.get(t.charAt(i)))
                return false;
        }
        
        return true;
    }
}
