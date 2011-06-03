public class Permute{
    public static void main(String[] args){
        int len = args[0].length();
        boolean [] used = new boolean[len];
        StringBuffer out = new StringBuffer();
        char[] in = args[0].toCharArray();

        doPermute(in, out, used, len, 0);
    }

    private static void doPermute(char[] in, StringBuffer out,
        boolean[] used, int length, int level){
        System.out.println("out: "+out);
        System.out.println("level: "+level);
        if (level == length){
            System.out.println("out: "+out);
            return;
        }
        for (int i=0; i<length; i++){
            if (used[i]) continue;
            out.append(in[i]);
            used[i] = true;
            doPermute(in, out, used, length, level+1);
            used[i] = false;
            out.setLength(out.length()-1);
        }
    }
} 
