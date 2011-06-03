void main(){
    char *str = "abcd";
    reverse(str);
}
void reverse(char* str){
    char tmp;
    char* end = str;
    if (str){
        while(*end){
            end++;
        }
        end--;
        while (str < end){
            tmp = *str;
            *str++ = *end;
            *end-- = tmp;
        }
    }
}
