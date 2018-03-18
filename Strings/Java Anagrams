static boolean isAnagram(String a, String b) {

        if (a.length() != b.length()) return false;
        
        a = a.toLowerCase();
        b = b.toLowerCase();
        
        int [] temp = new int [Character.MAX_VALUE]; 
        int sum = 0;

        for (int i = 0; i < a.length(); i++){
            sum += ++temp [a.charAt(i)] <= 0 ? -1 : 1;
            sum += --temp [b.charAt(i)] >= 0 ? -1 : 1;
        }

        return sum == 0;
        
}
