public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
        {
            return false;
        }

        int[] seen = new int[26];

        for (int i = 0; i < s.Length; i++)
        {
            seen[s[i] - 'a']++;
            seen[t[i] - 'a']--;
        }

        foreach (int num in seen)
        {
            if (num != 0)
            {
                return false;
            }
        }
        return true;
    }
}
