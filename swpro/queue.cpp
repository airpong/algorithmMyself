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
        if(front<0){
            printf("들어있는게 없어요.");
            return -1;
        }
        else return array[(front--)%100];
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
    printf("pop %d\n",st.pop());
    printf("pop %d\n",st.pop());
    printf("pop %d\n",st.pop());

    return 0;
}