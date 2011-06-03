public class CheckRotate{
    public static void main(String[] args){
        String s1 = args[0];
        String s2 = args[1];
        if (s1.length() != s2.length()){
            System.out.println("NO");
            return;
        }
        String s3 = s2+s2;
        if (s3.contains(s1)){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }
}
