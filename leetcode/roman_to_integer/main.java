class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> values = new LinkedHashMap<String, Integer>(){{
            put("M", 1000);
            put("CM", 900);
            put("D", 500);
            put("CD", 400);
            put("C", 100);
            put("XC", 90);
            put("L", 50);
            put("XL", 40);
            put("X", 10);
            put("IX", 9);
            put("V", 5);
            put("IV", 4);
            put("I", 1);
        }};

        int answer = 0;
        int offset = 0;

        while (s.length() > offset) {
            for (Map.Entry<String, Integer> entry : values.entrySet()) {
                if (s.startsWith(entry.getKey(), offset)){
                    offset += entry.getKey().length();
                    answer += entry.getValue();
                    break;
                }
            }
        }
        
        return answer;
    }
}