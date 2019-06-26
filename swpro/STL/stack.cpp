#include <stdio.h>
#include <iostream>
using namespace std;
class stack{
public:
    int front;
    int end;
    int array[100]={0,};
    stack() {
        printf("스택생성\n");
        front = -1;
        end = -1;
    }
    void push(int inp){
        array[(++front)%100]=inp;
    }
    int pop(){
        if((end+1)>front) printf("넣을수 있는 공간이 없습니다");
        else return array[(++end)%100];
    }
    int len(){
        return front-end;
    }
};
int main() {
    stack st = stack();
    st.push(3);
    st.push(5);
    printf("현재 길이는 : %d\n",st.len());
    printf("pop %d",st.pop());

    return 0;
}