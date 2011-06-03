public class Permute2{
    public static void main(String[] args){
        int len = args[0].length();
        StringBuffer out = new StringBuffer();
        char[] in = args[0].toCharArray();

        doPermute(in, out, used, len, 0);
    }

    private static void doPermute(char[] in, StringBuffer out,
        boolean[] used, int length, int index){
        if (index == length){
            return;
        }
        for (int i=index; i<length; i++){
            out.append(in[i]);
            System.out.println("out: "+out);
            doPermute(in, out, used, length, i+1);
            out.setLength(out.length()-1);
        }
    }
} 
