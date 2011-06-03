public class StringReverse{
    private static char tmp;
    public static void main(String[] args){
        for(int i=0 ; i<args.length ; i++){
            StringBuffer cur = new StringBuffer(args[0]);
            int len = cur.length();
            int numLoop = len/2;
            for (int j=0 ; j<numLoop ; j++){
                tmp = cur.charAt(j);
                cur.setCharAt(j,cur.charAt(len-1-j));
                cur.setCharAt(len-1-j, tmp);
            }
            System.out.println(cur);
        }
    }
}
